"
" Vim Configure
"
syntax on

set tabstop=4
set shiftwidth=4
set smarttab
set autoindent
set cindent
set cursorline
set nu
set incsearch
set hlsearch

" Set background light or dark
set bg=dark

" For powerline
set laststatus=2
set t_Co=256

" Replace tab to space when saving file.
autocmd FileType javascript,python set expandtab

nmap <F5> :NERDTree<CR>
nmap <F8> :TagbarToggle<CR>

" Gtags variables
let Gtags_Auro_Map = 1
let Gtags_Auto_Update = 1

" Gtags-cscope
let GtagsCscope_Auto_Map = 1
let GtagsCscope_Auto_Load = 1
set cscopetag

" IndentLine
let g:indentLine_char="│"


"
" Vundle Vim Config
"
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}
" YouCompleteMe
Plugin 'Valloric/YouCompleteMe'
" apiblueprint plugin
Plugin 'kylef/apiblueprint.vim'
" Tagbar: a class outline viewer for Vim
" https://github.com/majutsushi/tagbar
Plugin 'majutsushi/tagbar'
" For JavaScript
Plugin 'marijnh/tern_for_vim'
" tree directory
Plugin 'scrooloose/nerdtree'
" status line
Plugin 'Lokaltog/vim-powerline'
" show trail space
Plugin 'bronson/vim-trailing-whitespace'
" show indent line
Plugin 'Yggdroot/indentLine'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" YouCompleteMe Configure
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/.ycm_extra_conf.py'
let g:ycm_complete_in_comments=1   " auto complement in comments
let g:ycm_complete_in_strings = 1
let g:ycm_collect_identifiers_from_tags_files=1
let g:ycm_seed_identifiers_with_syntax=1
set completeopt=longest,menu

