ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

[ ! -d "$ZINIT_HOME" ] && mkdir -p "$(dirname "$ZINIT_HOME")"
[ ! -d "$ZINIT_HOME/.git" ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"

source "${ZINIT_HOME}/zinit.zsh"

zinit load zdharma-continuum/history-search-multi-word
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-syntax-highlighting

setopt PROMPT_SUBST
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
setopt SHARE_HISTORY

HISTFILE="${XDG_STATE_HOME:-$HOME/.local/state}/zsh/history"
mkdir -p "${HISTFILE:h}"
HISTSIZE=10000
SAVEHIST=10000

alias -g n='nvim'

alias ls='eza --icons=always --color=always --git'
alias ll='eza -lah --icons=always --git'

eval "$(zoxide init zsh)"
alias cd='z'

export PATH="$PATH:$(go env GOPATH)/bin:$HOME/.local/bin"

autoload -Uz vcs_info

zstyle ':vcs_info:git:*' formats '%F{8}git:%b%f'
zstyle ':vcs_info:git:*' actionformats '%F{8}git:%b (%a)%f'

setopt PROMPT_SUBST

precmd() {
    vcs_info
}

PROMPT_FULL=$'\n%F{cyan}%1~%f ${vcs_info_msg_0_} %F{yellow}%*%f\n%F{magenta}λ%f '

PROMPT_TRANSIENT='%F{magenta}λ%f '

PROMPT="$PROMPT_FULL"

RPROMPT='%(?..%F{red}exit:%?%f)'

zle-line-init() {
    PROMPT="$PROMPT_FULL"
    zle reset-prompt
}

zle-line-finish() {
    PROMPT="$PROMPT_TRANSIENT"
    zle reset-prompt
}

zle -N zle-line-init
zle -N zle-line-finish
