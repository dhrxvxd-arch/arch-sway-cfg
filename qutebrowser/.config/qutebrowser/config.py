
config.load_autoconfig()

c.colors.webpage.darkmode.enabled = True

c.statusbar.show = "always"

c.tabs.show = "always"
c.tabs.position = "left"
c.tabs.width = 220
c.tabs.title.alignment = "left"
c.tabs.favicons.show = "always"
c.tabs.padding = {
    "top": 6,
    "bottom": 6,
    "left": 8,
    "right": 8
}

config.bind('<Ctrl-n>', 'config-cycle tabs.show always never')
config.bind('<Ctrl-t>', 'open -t')
config.bind('<Ctrl-w>', 'tab-close')

c.url.searchengines = {
    'DEFAULT': 'https://www.duckduckgo.com/search?q={}',
    'aw': 'https://archlinux.org/search/?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'g': 'https://www.duckduckgo.com/search?q={}'
}

config.bind('M', 'hint links spawn mpv {hint-url}')

startpage = 'file:///home/dhrxv/dev/startup-page/index.html'
c.url.start_pages = [startpage]
c.url.default_page = startpage

c.fonts.default_family = "Iosevka Nerd Font"
c.fonts.default_size = "11pt"

c.fonts.tabs.selected = "11pt 'Iosevka Nerd Font'"
c.fonts.tabs.unselected = "11pt 'Iosevka Nerd Font'"
c.fonts.statusbar = "11pt 'Iosevka Nerd Font'"
c.fonts.completion.entry = "11pt 'Iosevka Nerd Font'"
c.fonts.downloads = "11pt 'Iosevka Nerd Font'"
c.fonts.messages.info = "11pt 'Iosevka Nerd Font'"
c.fonts.hints = "bold 11pt 'Iosevka Nerd Font'"
c.fonts.web.family.fixed = "Iosevka Nerd Font"

bg = "#000000"
bg_alt = "#000000"
bg_brighter = "#222222"
fg = "#c1c1c1"
fg_darker = "#999999"
accent = "#5f8787"
border = "#333333"

c.colors.webpage.bg = bg

c.colors.statusbar.normal.bg = bg
c.colors.statusbar.normal.fg = fg
c.colors.statusbar.insert.bg = accent
c.colors.statusbar.insert.fg = bg
c.colors.statusbar.command.bg = bg_alt
c.colors.statusbar.command.fg = fg
c.colors.statusbar.caret.bg = bg_brighter
c.colors.statusbar.caret.fg = fg
c.colors.statusbar.url.success.http.fg = fg
c.colors.statusbar.url.success.https.fg = fg

c.colors.tabs.bar.bg = bg_alt
c.colors.tabs.even.bg = bg_alt
c.colors.tabs.even.fg = fg_darker
c.colors.tabs.odd.bg = bg_alt
c.colors.tabs.odd.fg = fg_darker
c.colors.tabs.selected.even.bg = bg
c.colors.tabs.selected.even.fg = fg
c.colors.tabs.selected.odd.bg = bg
c.colors.tabs.selected.odd.fg = fg

c.colors.completion.category.bg = bg_alt
c.colors.completion.category.fg = fg
c.colors.completion.category.border.bottom = border

c.colors.completion.even.bg = bg
c.colors.completion.odd.bg = bg_alt
c.colors.completion.fg = fg

c.colors.completion.item.selected.bg = accent
c.colors.completion.item.selected.fg = bg
c.colors.completion.item.selected.border.top = accent
c.colors.completion.item.selected.border.bottom = accent

c.colors.completion.scrollbar.bg = bg_alt
c.colors.completion.scrollbar.fg = fg

c.colors.hints.bg = accent
c.colors.hints.fg = bg
c.colors.hints.match.fg = fg

c.colors.downloads.bar.bg = bg
c.colors.downloads.start.bg = accent
c.colors.downloads.start.fg = bg
c.colors.downloads.stop.bg = bg_alt
c.colors.downloads.stop.fg = fg

c.statusbar.show = "always"

c.statusbar.padding = {
    "top": 4,
    "bottom": 4,
    "left": 10,
    "right": 10
}

c.statusbar.widgets = [
    "keypress",
    "url",
    "scroll"
]

