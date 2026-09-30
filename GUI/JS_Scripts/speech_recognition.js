(function () {
  'use strict';
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    console.log('Web Speech API не поддерживается в этом браузере');
    return;
  }

  const recognition = new SpeechRecognition();

  // Настройки
  recognition.continuous = true;      
  recognition.interimResults = true;  
  recognition.lang = 'ru-RU';         

  // Обработка результатов
  recognition.onresult = async function (event) {
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const result = event.results[i];
      // В Chrome/Edge текст лежит в result[0].transcript
      const transcript = (result[0] && result[0].transcript) || '';

      if (result.isFinal) {
        console.log('Распознано:', transcript);
        const resultPy = await eel.process_text(transcript)
      } else {
        console.log('Промежуточный результат:', transcript);
      }
    }
  };

  recognition.onerror = function (event) {
    console.error('Ошибка распознавания:', event.error, event.message);
  };

  recognition.onend = function () {
    console.log('Сессия распознавания завершена');
  };
  const startBtn = document.getElementById('startButton');
  const stopBtn = document.getElementById('stopButton');

  if (startBtn) {
    startBtn.addEventListener('click', () => {
      if (recognition.readyState === 'started' || recognition.readyState === 'running') {
        console.log('Распознавание уже идёт');
        return;
      }
      recognition.start();
      startBtn.style.display = "none";
      stopBtn.style.display = "block";
    });
  }

  if (stopBtn) {
    stopBtn.addEventListener('click', () => {
      recognition.stop();
      startBtn.style.display = "block";
      stopBtn.style.display = "none";
    });
  }
})();
document.getElementById('inputText').addEventListener('keydown', async function (event) {
  if (event.keyCode == '13') {
    const text = document.getElementById('inputText').value;
    const result = await eel.process_text(text);
    document.getElementById('inputText').value = '';
  }
});