" Configuration file for vim
set modelines=0  " CVE-2007-2438

" Normally we use vim-extensions. If you want true vi-compatibility remove
" change the following statements
set nocompatible  " Use Vim defaults instead of 100% vi compatibility
set backspace=2  " More powerful backspacing

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

" Enable eouse
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
call pathogen#helptags()

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

" Settings for Auto Pairs
" cd ~/.vim/bundle
" git clone git://github.com/jiangmiao/auto-pairs.git ~/.vim/bundle/auto-pairs

" Settings for Jedi-Vim
" cd ~/.vim/bundle
" git clone --recursive https://github.com/davidhalter/jedi-vim.git ~/.vim/bundle/jedi-vim
" cd ~/.vim/bundle/jedi-vim
" git submodule update --init
let g:jedi#use_tabs_not_buffers = 1

" Settings for Python foldering
" mkdir -p ~/.vim/ftplugin
" wget -O ~/.vim/ftplugin/python_editing.vim http://www.vim.org/scripts/download_script.php?src_id=5492
set nofoldenable

" Settings for Python indent guides
" cd ~/.vim/bundle
" git clone git://github.com/nathanaelkane/vim-indent-guides.git
set ts=4 sw=4 et
let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_start_level = 2
let g:indent_guides_guide_size = 1

" Settings for vim-isort
" cd ~/.vim/bundle
" git clone git@github.com:fisadev/vim-isort.git
" To use it, just call the :Isort command
" Or, just call :%!isort - command

" Settings for vim-flake8
" cd ~/.vim/bundle
" git clone git@github.com:nvie/vim-flake8.git
let g:flake8_quickfix_location="topleft"
let g:flake8_show_in_file=1
let g:flake8_show_in_gutter=1
" To use it, just press \8 to call it
autocmd FileType python map <Leader>8 :call Flake8()<CR>
" Automatically call Flake8 when saving Python files
autocmd BufWritePost *.py call Flake8()

" Settings for vim-json
" (Better display JSON files)
" cd ~/.vim/bundle
" git clone git@github.com:elzr/vim-json.git

" Setting for vim-markdown
" cd ~/.vim/bundle
" git clone git@github.com:plasticboy/vim-markdown.git
let g:vim_markdown_math=1
let g:vim_markdown_json_frontmatter=1

" Setting for vim-gitgutter
" cd ~/.vim/bundle
" git clone git://github.com/airblade/vim-gitgutter.git
