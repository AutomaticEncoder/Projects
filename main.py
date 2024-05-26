import webbrowser
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
webbrowser.get('Chrome').open_new_tab('https://gist.github.com/idprogramming8/8d30520da3178df4ed7f24c15df12bbc')
