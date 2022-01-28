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
autocmd FileType html,xhtml,xml,xslt,xsd,javascript set expandtab
autocmd FileType perl,python,java set expandtab

" Other filetypes where we want spaces instead of tabs
autocmd FileType markdown,yaml set expandtab shiftwidth=2

nmap <F5> :NERDTree<CR>
nmap <F8> :Vista<CR>

" Gtags variables
let Gtags_Auro_Map = 1
let Gtags_Auto_Update = 1

" Gtags-cscope
let GtagsCscope_Auto_Map = 1
let GtagsCscope_Auto_Load = 1
set cscopetag

" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" Make sure you use single quotes

" YouCompleteMe
Plug 'Valloric/YouCompleteMe'

" apiblueprint plugin
Plug 'kylef/apiblueprint.vim'

" Tagbar
Plug 'liuchengxu/vista.vim'

" For JavaScript
Plug 'marijnh/tern_for_vim'

" tree directory
Plug 'scrooloose/nerdtree'

" status line
Plug 'Lokaltog/vim-powerline'

" show trail space
Plug 'bronson/vim-trailing-whitespace'

" show indent line
Plug 'Yggdroot/indentLine'

" Initialize plugin system
call plug#end()

" IndentLine Configure
let g:indentLine_char="│"

" YouCompleteMe Configure
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/.ycm_extra_conf.py'
let g:ycm_complete_in_comments = 1   " auto complement in comments
let g:ycm_complete_in_strings = 1
let g:ycm_collect_identifiers_from_tags_files=1
let g:ycm_seed_identifiers_with_syntax=1
set completeopt=longest,menu

" vista.vim Configure
function! NearestMethodOrFunction() abort
	return get(b:, 'vista_nearest_method_or_function', '')
endfunction

set statusline+=%{NearestMethodOrFunction()}

" By default vista.vim never run if you don't call it explicitly.
"
" If you want to show the nearest function in your statusline automatically,
" you can add the following line to your vimrc
autocmd VimEnter * call vista#RunForNearestMethodOrFunction()

" Executive used when opening vista sidebar without specifying it.
" See all the avaliable executives via `:echo g:vista#executives`.
let g:vista_default_executive = 'ctags'

" The default icons can't be suitable for all the filetypes, you can extend it as you wish.
let g:vista#renderer#icons = {
\   "function": "\uf794",
\   "variable": "\uf71b",
\  }

" Disable the icon in vista.vim
let g:vista#renderer#enable_icon = 0

