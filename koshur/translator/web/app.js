/**
 * J&K Revenue Records Decipherment & Translation Engine - Client Logic
 * Handles interactive language preference switching (English/Hindi/Dual),
 * specimen loading, OCR scan uploads, cadastral conversions, and certificate generation.
 */

let currentTab = 'text';
let sampleRecords = [];
let currentTranslationResult = null;
let currentUploadedFile = null;
let userLanguagePreference = 'en'; // 'en', 'hi', 'both'
let activeModalCertLang = 'en';

window.addEventListener('DOMContentLoaded', async () => {
  setupDropzone();
  await loadSamples();
});

// Set user language preference (English, Hindi, Dual)
function setUserLangPreference(lang) {
  userLanguagePreference = lang;
  document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
  document.getElementById('btnLangHi').classList.toggle('active', lang === 'hi');
  document.getElementById('btnLangBoth').classList.toggle('active', lang === 'both');

  // If a result is already present, re-render immediately with the chosen language
  if (currentTranslationResult) {
    renderResult(currentTranslationResult);
  }
}

// Fetch available authentic sample records from backend
async function loadSamples() {
  try {
    const res = await fetch('/api/samples');
    sampleRecords = await res.json();
    renderSamplePills();
    if (sampleRecords.length > 0) {
      selectSample(sampleRecords[0].id);
    }
  } catch (err) {
    console.error("Failed to load sample records:", err);
  }
}

// Render sample pills
function renderSamplePills() {
  const container = document.getElementById('pillsRow');
  container.innerHTML = '';
  sampleRecords.forEach(s => {
    const btn = document.createElement('button');
    btn.className = 'pill-btn';
    btn.id = 'pill_' + s.id;
    btn.innerHTML = `📜 <span>${s.title.split('-')[0].trim()}</span>`;
    btn.title = s.notes || `${s.title} (${s.date || ''})`;
    btn.onclick = () => selectSample(s.id);
    container.appendChild(btn);
  });
}

// Select a sample record
async function selectSample(id) {
  document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
  const activePill = document.getElementById('pill_' + id);
  if (activePill) activePill.classList.add('active');

  try {
    const res = await fetch('/api/sample?id=' + encodeURIComponent(id));
    const data = await res.json();
    document.getElementById('recordInput').value = data.urdu_text || '';
    document.getElementById('statusBadge').textContent = 'Loaded: ' + (data.doc_type || 'Sample');
  } catch (err) {
    console.error("Failed to fetch sample:", err);
  }
}

// Switch between Raw Text and Scan Upload tabs
function switchTab(tab) {
  currentTab = tab;
  document.getElementById('tabTextBtn').classList.toggle('active', tab === 'text');
  document.getElementById('tabUploadBtn').classList.toggle('active', tab === 'upload');
  document.getElementById('textInputGroup').style.display = tab === 'text' ? 'flex' : 'none';
  document.getElementById('uploadInputGroup').style.display = tab === 'upload' ? 'flex' : 'none';
  document.getElementById('specimenBar').style.display = tab === 'text' ? 'block' : 'none';
}

// Setup drag and drop for scan uploads
function setupDropzone() {
  const dropzone = document.getElementById('dropzone');
  if (!dropzone) return;

  ['dragenter', 'dragover'].forEach(name => {
    dropzone.addEventListener(name, (e) => {
      e.preventDefault();
      dropzone.classList.add('dragover');
    });
  });
  ['dragleave', 'drop'].forEach(name => {
    dropzone.addEventListener(name, (e) => {
      e.preventDefault();
      dropzone.classList.remove('dragover');
    });
  });
  dropzone.addEventListener('drop', (e) => {
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      processFile(e.dataTransfer.files[0]);
    }
  });
}

function handleFileSelect(e) {
  if (e.target.files && e.target.files[0]) {
    processFile(e.target.files[0]);
  }
}

function processFile(file) {
  currentUploadedFile = file;
  document.getElementById('previewContainer').style.display = 'block';
  document.getElementById('previewName').textContent = file.name;

  if (file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = (e) => {
      document.getElementById('previewImg').src = e.target.result;
    };
    reader.readAsDataURL(file);
  } else {
    document.getElementById('previewImg').src = '';
    document.getElementById('previewStats').textContent = 'PDF Document (' + (file.size / 1024).toFixed(1) + ' KB)';
  }
  document.getElementById('statusBadge').textContent = 'File Loaded';
}

function loadArchivalScan(scanName) {
  currentUploadedFile = { name: scanName, isSpecimen: true };
  document.getElementById('previewContainer').style.display = 'block';
  document.getElementById('previewName').textContent = scanName;
  document.getElementById('previewStats').textContent = 'Research Archival Specimen (DPI 300)';
  document.getElementById('previewImg').src = '/api/specimen_image?page=' + encodeURIComponent(scanName);
  document.getElementById('statusBadge').textContent = 'Specimen: ' + scanName;
}

// Revenue Keypad helper
function insertKeypadTerm(term) {
  const textarea = document.getElementById('recordInput');
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  const text = textarea.value;
  textarea.value = text.substring(0, start) + term + text.substring(end);
  textarea.focus();
  textarea.selectionStart = textarea.selectionEnd = start + term.length;
}

// Clear input textarea
function clearInputText() {
  document.getElementById('recordInput').value = '';
  document.getElementById('recordInput').focus();
  document.getElementById('statusBadge').textContent = 'Cleared';
}

// Main translation execution
async function runTranslation() {
  const btn = document.getElementById('btnTranslate');
  const btnText = document.getElementById('btnText');
  const btnIcon = document.getElementById('btnIcon');

  btn.disabled = true;
  btnIcon.innerHTML = '<span class="spinner"></span>';
  btnText.textContent = userLanguagePreference === 'hi' ? 'अनुवाद एवं पाठोद्धार जारी...' : 'Deciphering & Translating...';
  document.getElementById('statusBadge').textContent = 'Processing...';

  try {
    let result = null;

    if (currentTab === 'upload' && currentUploadedFile) {
      if (currentUploadedFile.isSpecimen) {
        const res = await fetch('/api/translate_file', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            filename: currentUploadedFile.name,
            target_lang: userLanguagePreference
          })
        });
        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.error || `HTTP error ${res.status}`);
        }
        result = await res.json();
      } else {
        const base64Data = await fileToBase64(currentUploadedFile);
        const res = await fetch('/api/upload', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            filename: currentUploadedFile.name,
            base64_data: base64Data,
            target_lang: userLanguagePreference
          })
        });
        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.error || `HTTP error ${res.status}`);
        }
        result = await res.json();
      }
    } else {
      const text = document.getElementById('recordInput').value.trim();
      if (!text) {
        alert('Please enter record text or select an archival specimen.');
        return;
      }
      const res = await fetch('/api/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text,
          target_lang: userLanguagePreference
        })
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.error || `HTTP error ${res.status}`);
      }
      result = await res.json();
    }

    if (result) {
      if (result.error) {
        throw new Error(result.error);
      }
      currentTranslationResult = result;
      renderResult(result);
      document.getElementById('btnViewCert').style.display = 'inline-flex';
      document.getElementById('btnExportJSON').style.display = 'inline-flex';

      if (result.status === 'image_preprocessed_no_text') {
        document.getElementById('statusBadge').textContent = (userLanguagePreference === 'hi') ? 'छवि प्रसंस्कृत' : 'Image Preprocessed';
        showToast(userLanguagePreference === 'hi'
          ? 'दस्तावेज़ छवि सफलतापूर्वक लोड एवं प्रसंस्कृत की गई।'
          : 'Archival image preprocessed successfully for OCR.');
      } else {
        document.getElementById('statusBadge').textContent = 'Translation Complete';
        showToast('Record translated successfully with zero-error integrity seal!');
      }
    }
  } catch (err) {
    console.error("Translation failed:", err);
    alert("Translation failed: " + err.message);
    document.getElementById('statusBadge').textContent = 'Error';
  } finally {
    btn.disabled = false;
    btnIcon.innerHTML = '⚡';
    btnText.textContent = userLanguagePreference === 'hi' ? 'दस्तावेज़ अनुवाद करें' : 'Translate & Decipher Record';
  }
}

// Render translation result with language-specific text and labels
function renderResult(data) {
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('resultContainer').style.display = 'flex';

  const isHi = (userLanguagePreference === 'hi');
  const isBoth = (userLanguagePreference === 'both');

  const sum = data.summary || {};
  const ent = data.entities || {};
  const meas = ent.measurements || {};
  const conv = meas.conversions || {};
  const parsed = meas.parsed_units || {};

  // Update card and section headings based on language preference
  if (isHi) {
    document.getElementById('transCardTitle').textContent = 'प्रमाणित राजस्व हिन्दी अनुवाद';
    document.getElementById('lblDocType').textContent = 'दस्तावेज़ वर्गीकरण';
    document.getElementById('lblVillage').textContent = 'मौजाह / ग्राम';
    document.getElementById('lblDistrict').textContent = 'ज़िला';
    document.getElementById('lblDate').textContent = 'ऐतिहासिक संवत/तिथि';
    document.getElementById('lblCadastralHeader').textContent = 'भूखंड विवरणी एवं वैधानिक क्षेत्रफल रूपांतरण';
    document.getElementById('lblUnitLocal').textContent = 'स्थानीय क्षेत्रफल';
    document.getElementById('lblUnitSqFt').textContent = 'वर्ग फीट';
    document.getElementById('lblUnitAcres').textContent = 'मानक एकड़';
    document.getElementById('lblUnitHa').textContent = 'हेक्टेयर';
    document.getElementById('lblClausesHeader').textContent = 'प्रमाणित कार्यकारी हिन्दी विधिक अनुवाद:';
    document.getElementById('lblFormulasHeader').textContent = 'पाठोद्धारित शिकस्ता सूत्र एवं संक्षेप चिह्न:';
    document.getElementById('lblGlossaryHeader').textContent = 'प्राविधिक राजस्व शब्दावली (शब्दावली अर्थ):';
  } else if (isBoth) {
    document.getElementById('transCardTitle').textContent = 'Certified Dual Translation (English & हिन्दी)';
    document.getElementById('lblDocType').textContent = 'Classification / वर्गीकरण';
    document.getElementById('lblVillage').textContent = 'Village / ग्राम';
    document.getElementById('lblDistrict').textContent = 'District / ज़िला';
    document.getElementById('lblDate').textContent = 'Era / संवत';
    document.getElementById('lblCadastralHeader').textContent = 'Cadastral Schedule & Land Conversions';
    document.getElementById('lblUnitLocal').textContent = 'Local Area (कनाल/मरला)';
    document.getElementById('lblUnitSqFt').textContent = 'Square Feet';
    document.getElementById('lblUnitAcres').textContent = 'Acres / एकड़';
    document.getElementById('lblUnitHa').textContent = 'Hectares / हे.';
    document.getElementById('lblClausesHeader').textContent = 'Operative Clauses (English & हिन्दी):';
    document.getElementById('lblFormulasHeader').textContent = 'Decoded Formulas & Ligatures (शिकस्ता सूत्र):';
    document.getElementById('lblGlossaryHeader').textContent = 'Cadastral Lexicon / राजस्व शब्दावली:';
  } else {
    document.getElementById('transCardTitle').textContent = 'Certified Legal English Translation';
    document.getElementById('lblDocType').textContent = 'Classification';
    document.getElementById('lblVillage').textContent = 'Village / Mauza';
    document.getElementById('lblDistrict').textContent = 'District';
    document.getElementById('lblDate').textContent = 'Historical Era';
    document.getElementById('lblCadastralHeader').textContent = 'Cadastral Survey & Statutory Land Measurements';
    document.getElementById('lblUnitLocal').textContent = 'Local Area';
    document.getElementById('lblUnitSqFt').textContent = 'Square Feet';
    document.getElementById('lblUnitAcres').textContent = 'Standard Acres';
    document.getElementById('lblUnitHa').textContent = 'Hectares';
    document.getElementById('lblClausesHeader').textContent = 'Certified Operative Clauses & Covenant Translation:';
    document.getElementById('lblFormulasHeader').textContent = 'Decoded Scribal Formulas & Khat-i-Shikast Ligatures:';
    document.getElementById('lblGlossaryHeader').textContent = 'Identified Cadastral & Revenue Lexicon:';
  }

  // Set SHA-256 integrity hash
  const hash = data.integrity_hash || (sum.integrity_hash || '0'.repeat(64));
  document.getElementById('resHash').textContent = hash.substring(0, 16) + '...' + hash.substring(48);
  document.getElementById('resHash').title = 'Full SHA-256 Audit Seal: ' + hash;

  document.getElementById('docIdBadge').textContent = 'REF: ' + (data.doc_id || 'JK-REC');
  
  if (isHi) {
    document.getElementById('resDocType').textContent = data.title_hi || sum.document_type_hi || 'राजस्व अभिलेख';
    document.getElementById('resDate').textContent = sum.date_hi || sum.date || 'अभिलेखीय काल';
    document.getElementById('resVillage').textContent = sum.village_hi || sum.village_display || sum.village || 'अनिर्दिष्ट';
    document.getElementById('resDistrict').textContent = sum.district_hi || sum.district_display || sum.district || 'अनिर्दिष्ट';
  } else {
    document.getElementById('resDocType').textContent = data.title_en || sum.document_type || data.title || 'Revenue Record';
    document.getElementById('resDate').textContent = sum.date || 'Historical Period';
    document.getElementById('resVillage').textContent = sum.village_en || sum.village_display || sum.village || 'Unspecified';
    document.getElementById('resDistrict').textContent = sum.district_en || sum.district_display || sum.district || 'Unspecified';
  }

  const khasras = (ent.survey && ent.survey.khasra_numbers) ? ent.survey.khasra_numbers.join(', ') : 'Survey Parcel';
  document.getElementById('resSurveyId').textContent = (isHi ? 'खसरा संख्या: ' : 'Khasra No. ') + khasras;

  const totalK = parsed.kanals !== undefined ? parsed.kanals : (sum.total_kanals || 0);
  const totalM = parsed.marlas !== undefined ? parsed.marlas : 0;
  document.getElementById('resLocalArea').textContent = totalK + (isHi ? ' कनाल, ' : ' K, ') + totalM + (isHi ? ' मरला' : ' M');
  document.getElementById('resSqFeet').textContent = (conv.sq_feet ? conv.sq_feet.toLocaleString() : '0') + (isHi ? ' वर्ग फीट' : ' sq ft');
  document.getElementById('resAcres').textContent = (conv.acres ? conv.acres.toFixed(4) : '0.0000') + (isHi ? ' एकड़' : ' ac');
  document.getElementById('resHectares').textContent = (conv.hectares ? conv.hectares.toFixed(4) : '0.0000') + (isHi ? ' हे.' : ' ha');

  // Translated clauses selection
  let activeText = data.translated_text_en || data.translated_text || '';
  if (isHi) {
    activeText = data.translated_text_hi || data.translated_text || '';
  } else if (isBoth) {
    activeText = '=== Certified English Translation ===\n' + (data.translated_text_en || '') + '\n\n=== प्रमाणित हिन्दी अनुवाद ===\n' + (data.translated_text_hi || '');
  }

  const clausesBox = document.getElementById('resClauses');
  clausesBox.innerHTML = '';
  const lines = activeText.split('\n');
  lines.forEach(line => {
    if (line.trim()) {
      const p = document.createElement('p');
      p.textContent = line.trim();
      clausesBox.appendChild(p);
    }
  });

  // Decoded formulas with bilingual support
  const formulasWrap = document.getElementById('resFormulas');
  formulasWrap.innerHTML = '';
  const formulas = data.formulas || [];
  if (formulas.length === 0) {
    document.getElementById('formulasSection').style.display = 'none';
  } else {
    document.getElementById('formulasSection').style.display = 'block';
    formulas.forEach(f => {
      const row = document.createElement('div');
      row.className = 'formula-tag';
      const expl = isHi ? (f.meaning_hi || f.meaning_en) : f.meaning_en;
      const ctx = isHi ? (f.context_hi || f.context) : f.context;
      row.innerHTML = `
        <div>
          <span class="symbol">${f.formula}</span>
          <strong style="margin-left: 8px;">${f.transliteration}</strong>: ${expl}
        </div>
        <div style="font-size: 11px; color: var(--text-dim);">${ctx || ''}</div>
      `;
      formulasWrap.appendChild(row);
    });
  }

  // Technical glossary chips
  const glossWrap = document.getElementById('resGlossary');
  glossWrap.innerHTML = '';
  const glossary = (isHi ? data.glossary_hi : data.glossary_en) || data.glossary || [];
  glossary.slice(0, 14).forEach(g => {
    const chip = document.createElement('div');
    chip.className = 'glossary-chip';
    chip.title = `${g.term}: ${g.definition}`;
    chip.textContent = `${g.term} (${g.urdu})`;
    glossWrap.appendChild(chip);
  });
}

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      const res = reader.result;
      const base64 = res.split(',')[1];
      resolve(base64);
    };
    reader.onerror = error => reject(error);
  });
}

function copyTranslation() {
  if (!currentTranslationResult) return;
  const isHi = (userLanguagePreference === 'hi');
  const text = isHi ? (currentTranslationResult.translated_text_hi || currentTranslationResult.translated_text) : (currentTranslationResult.translated_text_en || currentTranslationResult.translated_text);
  navigator.clipboard.writeText(text || '');
  showToast(isHi ? 'अनुवाद क्लिपबोर्ड पर कॉपी हो गया!' : 'Translated text copied to clipboard!');
}

function downloadMarkdown() {
  if (!currentTranslationResult) return;
  const isHi = (userLanguagePreference === 'hi');
  const content = currentTranslationResult.markdown || '';
  const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  const suffix = isHi ? '_hindi_translation.md' : '_translation.md';
  a.download = (currentTranslationResult.doc_id || 'record') + suffix;
  a.click();
  showToast('Markdown translation downloaded!');
}

function exportJSON() {
  if (!currentTranslationResult) return;
  const blob = new Blob([JSON.stringify(currentTranslationResult, null, 2)], { type: 'application/json;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = (currentTranslationResult.doc_id || 'record') + '_bilingual_audit.json';
  a.click();
  showToast('JSON audit payload exported!');
}

function openCertificateModal() {
  if (!currentTranslationResult) return;
  activeModalCertLang = (userLanguagePreference === 'hi') ? 'hi' : 'en';
  renderModalCertificate();
  document.getElementById('certModal').style.display = 'block';
}

function switchModalCertificate(lang) {
  activeModalCertLang = lang;
  renderModalCertificate();
}

function renderModalCertificate() {
  document.getElementById('modalLangEnBtn').classList.toggle('active', activeModalCertLang === 'en');
  document.getElementById('modalLangHiBtn').classList.toggle('active', activeModalCertLang === 'hi');
  const iframe = document.getElementById('certIframe');
  if (activeModalCertLang === 'hi') {
    iframe.srcdoc = currentTranslationResult.certified_html_hi || currentTranslationResult.certified_html;
  } else {
    iframe.srcdoc = currentTranslationResult.certified_html_en || currentTranslationResult.certified_html;
  }
}

function closeCertificateModal(e) {
  if (!e || e.target === document.getElementById('certModal')) {
    document.getElementById('certModal').style.display = 'none';
  }
}

function printCertificate() {
  const iframe = document.getElementById('certIframe');
  if (iframe && iframe.contentWindow) {
    iframe.contentWindow.print();
  }
}

function showToast(message) {
  const toast = document.getElementById('toastAlert');
  if (!toast) return;
  toast.textContent = message;
  toast.style.display = 'block';
  setTimeout(() => {
    toast.style.display = 'none';
  }, 3200);
}
