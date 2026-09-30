document.getElementById('commandButton').addEventListener('click', () => {
  const mainMenu = document.getElementById('mainWrapper');
  const commandMenu = document.getElementById('messageWrapper');
  if (commandMenu.style.display == "none") {
    mainMenu.style.display = "none";
    commandMenu.style.display = "block";
  }
});
document.getElementById('closeButtonMessage').addEventListener('click', () => {
  const mainMenu = document.getElementById('mainWrapper');
  const commandMenu = document.getElementById('messageWrapper');
  if (mainMenu.style.display == "none") {
    commandMenu.style.display = "none";
    mainMenu.style.display = "block";
  }
});
eel.get_time_commands()(commands => {
  const list = document.getElementById('time-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_date_commands()(commands => {
  const list = document.getElementById('date-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_music_on_commands()(commands => {
  const list = document.getElementById('music-on-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_music_off_commands()(commands => {
  const list = document.getElementById('music-off-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_music_other_commands()(commands => {
  const list = document.getElementById('music-other-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_music_that_commands()(commands => {
  const list = document.getElementById('music-that-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_game_commands()(commands => {
  const list = document.getElementById('game-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_search_commands()(commands => {
  const list = document.getElementById('search-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});
eel.get_site_open_commands()(commands => {
  const list = document.getElementById('site-open-commands-list');
  if (!list) return;

  commands.forEach(cmd => {
    const li = document.createElement('h4');
    li.textContent = cmd;
    list.appendChild(li);
  });
});