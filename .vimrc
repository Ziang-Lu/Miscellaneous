" Configuration file for vim
set modelines=0		" CVE-2007-2438

" Normally we use vim-extensions. If you want true vi-compatibility remove
" change the following statements
set nocompatible	" Use Vim defaults instead of 100% vi compatibility
set backspace=2		" More powerful backspacing

" Don't write backup file if vim is being called by "crontab -e"
au BufWrite /private/tmp/crontab.* set nowritebackup nobackup
" Don't write backup file if vim is being called by "chpass"
au BufWrite /private/etc/pw.* set nowritebackup nobackup

" Set encoding
set encoding=utf-8
set fileencodings=utf-8,ucs-bom,cp936,gb18030,gb2312,gbk
set termencoding=utf-8

" Enable syntax highlighting
filetype off
filetype plugin indent on
syntax enable
syntax on

" Highlight matched brackets
set showmatch

" Set tab width
set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4
set shiftround

" Set auto-indent
set autoindent
set smartindent

" Display line numbers
set number

" Display cursor
set cursorline

" Display ruler
set ruler
set colorcolumn=80
highlight ColorColumn ctermbg=233

" Do not automatically wrap lines on load
set nowrap

" Show whitespace (MUST insert BEFORE colorscheme command)
autocmd ColorScheme * highlight ExtraWhitespace ctermbg=red guibg=red
au InsertLeave * match ExtraWhitespace /\s\+$/

" Allow folding
set foldenable

" Enable mouse
set mouse=a

" Ignore upper/lower case when searching
set ignorecase
set smartcase

" Highlight keywords when searching
set hlsearch

" Better copy & paste
set clipboard=unnamed

" Display vim mode
set showmode

" Set colorscheme
" mkdir -p ~/.vim/colors && cd ~/.vim/colors
" wget -O wombat256mod.vim
" http://www.vim.org/scripts/download_script.php?src_id=13400
set t_Co=256
color wombat256mod

" Avoid generating backup and swap files
set nobackup
set nowritebackup
set noswapfile

" Setup Pathogen to manage plugins
" mkdir -p ~/.vim/autoload ~/.vim/bundle
" curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
call pathogen#infect()

" Settings for vim-powerline
" (Display the current mode and current file)
" cd ~/.vim/bundle
" git clone git://github.com/Lokaltog/vim-powerline.git
set laststatus=2

" Settings for nerdtree
" (Shows the project structure)
" cd ~/.vim/bundle
" git clone git@github.com:scrooloose/nerdtree.git
autocmd vimenter * NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Settings for ctrlp
" (Quickly navigate through files and open files)
" cd ~/.vim/bundle
" git clone https://github.com/kien/ctrlp.vim.git
let g:ctrlp_max_height = 30
set wildignore+=*.pyc
set wildignore+=*_build/*
set wildignore+=*/coverage/*

