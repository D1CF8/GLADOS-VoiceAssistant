document.getElementById('settingsButton').addEventListener('click', () => {
  const mainMenu = document.getElementById('mainWrapper');
  const settingsMenu = document.getElementById('settingsWrapper');
  if (settingsMenu.style.display == "none") {
    mainMenu.style.display = "none";
    settingsMenu.style.display = "block";
  }
});
document.getElementById('closeButtonSettings').addEventListener('click', () => {
  const mainMenu = document.getElementById('mainWrapper');
  const settingsMenu = document.getElementById('settingsWrapper');
  if (settingsMenu.style.display == "block") {
    settingsMenu.style.display = "none";
    mainMenu.style.display = "block";
  }
});
function lockSize(width, height) {
  window.resizeTo(width, height);
  const check = () => {
    if (window.innerWidth !== width || window.innerHeight !== height) {
      window.resizeTo(width, height);
      window.moveTo(window.screenX, window.screenY); 
    }
  };
  setInterval(check, 200);
}

lockSize(600, 600);

eel.get_music_list()(commands => {
  const list = document.getElementById('music-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
}); 
eel.get_game_list()(commands => {
  const list = document.getElementById('game-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});

document.getElementById('voice').addEventListener('click', async () => {
  const mode = document.getElementById('voice').value;
  await eel.save_settings(mode);
  loadAndApplySettings();
});
document.getElementById('text').addEventListener("click", async () => {
  const mode = document.getElementById('text').value;
  await eel.save_settings(mode);
  loadAndApplySettings();
});
document.getElementById('light').addEventListener('click', async () => {
  const mode = document.getElementById('light').value;
  await eel.save_settings(mode);
  loadAndApplySettings();
});
document.getElementById('dark').addEventListener('click', async () => {
  const mode = document.getElementById('dark').value;
  await eel.save_settings(mode);
  loadAndApplySettings();
});
document.getElementById('dark-orange').addEventListener('click', async () => {
  const mode = document.getElementById('dark-orange').value;
  await eel.save_settings(mode);
  loadAndApplySettings();
});

function setActiveInputMode(mode) {
  const voiceInput = document.getElementById('voiceButton');
  const textInput = document.getElementById('inputText');
  const messageButton = document.getElementById('commandButtonWrapper');
  const settingsButton = document.getElementById('settingsButtonWrapper');
  if (mode == 'voice') {
    messageButton.classList.remove('textMessage');
    settingsButton.classList.remove('textSettings');
    voiceInput.style.display = "block";
    textInput.style.display = "none";
  } else {
    messageButton.classList.add('textMessage');
    settingsButton.classList.add('textSettings');
    voiceInput.style.display = "none";
    textInput.style.display = "block";
  }
}

function applyTheme(themeName) {
  const logo1 = document.getElementById('logo1');
  const logo2 = document.getElementById('logo2');
  const logo3 = document.getElementById('logo3');
  const voiceInputOn = document.getElementById('startButton');
  const voiceInputOff = document.getElementById('stopButton');
  const textInput = document.getElementById('inputText');
  const settingsButton = document.getElementById('settingsButton');
  const messageButton = document.getElementById('commandButton');
  const closeButtonMessage = document.getElementById('closeButtonMessage');
  const closeButtonSettings = document.getElementById('closeButtonSettings');
  const voiceButton = document.getElementById('voice');
  const textButton = document.getElementById('text');
  const lightButton = document.getElementById('light');
  const darkButton = document.getElementById('dark');
  const darkOrangeButton = document.getElementById('dark-orange');

  const lightColor = "#555555";
  const darkColor = "#0099FF";
  const darkOrangeColor = "#F9B400";
  const darkClassName = 'darkButton';
  const darkOrangeClassName = 'darkOrangeButton';
  const lightClassName = 'lightButton';
  if (themeName == "dark") {
    document.body.classList.remove("light");
    document.body.classList.remove("dark-orange");
    document.body.classList.add("dark");

    voiceButton.classList.remove(lightClassName);
    voiceButton.classList.remove(darkOrangeClassName);
    textButton.classList.remove(lightClassName);
    textButton.classList.remove(darkOrangeClassName)
    lightButton.classList.remove(lightClassName);
    lightButton.classList.remove(darkOrangeClassName);
    darkButton.classList.remove(lightClassName);
    darkButton.classList.remove(darkOrangeClassName);
    darkOrangeButton.classList.remove(lightClassName);
    darkOrangeButton.classList.remove(darkOrangeClassName);
    closeButtonMessage.classList.remove(lightClassName);
    closeButtonMessage.classList.remove(darkOrangeClassName);
    closeButtonSettings.classList.remove(lightClassName);
    closeButtonSettings.classList.remove(darkOrangeClassName);


    logo1.style.display = "none";
    logo2.style.display = "block";
    logo3.style.display = "none"; 

    voiceInputOn.style.color = darkColor;
    voiceInputOff.style.color = darkColor;
    settingsButton.style.color = darkColor;
    messageButton.style.color = darkColor;

    textInput.style.color = darkColor;
    textInput.style.borderColor = darkColor;

    voiceButton.classList.add(darkClassName);
    textButton.classList.add(darkClassName);

    lightButton.classList.add(darkClassName);
    darkButton.classList.add(darkClassName);
    darkOrangeButton.classList.add(darkClassName);

    closeButtonMessage.classList.add(darkClassName);
    closeButtonSettings.classList.add(darkClassName);


  }
  else if (themeName == "dark-orange")  {
    document.body.classList.remove("light");
    document.body.classList.add("dark-orange");
    document.body.classList.remove("dark");

    voiceButton.classList.remove(lightClassName);
    voiceButton.classList.remove(darkClassName);
    textButton.classList.remove(lightClassName);
    textButton.classList.remove(darkClassName)
    lightButton.classList.remove(lightClassName);
    lightButton.classList.remove(darkClassName);
    darkButton.classList.remove(lightClassName);
    darkButton.classList.remove(darkClassName);
    darkOrangeButton.classList.remove(lightClassName);
    darkOrangeButton.classList.remove(darkClassName);
    closeButtonMessage.classList.remove(lightClassName);
    closeButtonMessage.classList.remove(darkClassName);
    closeButtonSettings.classList.remove(lightClassName);
    closeButtonSettings.classList.remove(darkClassName);

    logo1.style.display = "none";
    logo2.style.display = "none";
    logo3.style.display = "block"; 

    voiceInputOn.style.color = darkOrangeColor;
    voiceInputOff.style.color = darkOrangeColor;
    settingsButton.style.color = darkOrangeColor;
    messageButton.style.color = darkOrangeColor;

    textInput.style.color = darkOrangeColor;
    textInput.style.borderColor = darkOrangeColor;

    voiceButton.classList.add(darkOrangeClassName);
    textButton.classList.add(darkOrangeClassName);

    lightButton.classList.add(darkOrangeClassName);
    darkButton.classList.add(darkOrangeClassName);
    darkOrangeButton.classList.add(darkOrangeClassName);

    closeButtonMessage.classList.add(darkOrangeClassName);
    closeButtonSettings.classList.add(darkOrangeClassName);
  }
  else {
    document.body.classList.add("light");
    document.body.classList.remove("dark-orange");
    document.body.classList.remove("dark");

    voiceButton.classList.remove(darkClassName);
    voiceButton.classList.remove(darkOrangeClassName);
    textButton.classList.remove(darkClassName);
    textButton.classList.remove(darkOrangeClassName)
    lightButton.classList.remove(darkClassName);
    lightButton.classList.remove(darkOrangeClassName);
    darkButton.classList.remove(darkClassName);
    darkButton.classList.remove(darkOrangeClassName);
    darkOrangeButton.classList.remove(darkClassName);
    darkOrangeButton.classList.remove(darkOrangeClassName);
    closeButtonMessage.classList.remove(darkClassName);
    closeButtonMessage.classList.remove(darkOrangeClassName);
    closeButtonSettings.classList.remove(darkClassName);
    closeButtonSettings.classList.remove(darkOrangeClassName);

    logo1.style.display = "block";
    logo2.style.display = "none";
    logo3.style.display = "none";

    voiceInputOn.style.color = lightColor;
    voiceInputOff.style.color = lightColor;
    settingsButton.style.color = lightColor;
    messageButton.style.color = lightColor;

    textInput.style.color = lightColor;
    textInput.style.borderColor = lightColor;

    voiceButton.classList.add(lightClassName);
    textButton.classList.add(lightClassName);

    lightButton.classList.add(lightClassName);
    darkButton.classList.add(lightClassName);
    darkOrangeButton.classList.add(lightClassName);

    closeButtonMessage.classList.add(lightClassName);
    closeButtonSettings.classList.add(lightClassName);
  }
}

function loadAndApplySettings() {
  eel.get_settings()(data => {
    setActiveInputMode(data.input_mode);
    applyTheme(data.theme);
  });
}

loadAndApplySettings();