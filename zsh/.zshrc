ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

[ ! -d "$ZINIT_HOME" ] && mkdir -p "$(dirname "$ZINIT_HOME")"
[ ! -d "$ZINIT_HOME/.git" ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"

source "${ZINIT_HOME}/zinit.zsh"

alias -g n='nvim'

eval "$(zoxide init zsh)"
alias cd="z"

alias ls="eza --icons=always --color=always --git"
alias ll="eza -lah --icons=always --git"

zinit load zdharma-continuum/history-search-multi-word
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-syntax-highlighting

autoload -Uz vcs_info

setopt PROMPT_SUBST

zstyle ':vcs_info:git:*' formats '%F{8}[%F{magenta}%b%F{8}]%f'

precmd() {
    vcs_info
}

PROMPT_FULL=$'\n%F{8}┌[%F{cyan}%n%F{8}]%f
%F{8}└%f%F{8}[%F{blue}%~%F{8}]%f
%F{magenta} λ%f '

PROMPT_TRANSIENT='%F{magenta}λ%f '

PROMPT="$PROMPT_FULL"

RPROMPT='%(?..%F{red}exit: %?%f) ${vcs_info_msg_0_}'

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

