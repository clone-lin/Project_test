call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes

" The NERDTree is a file system explorer for the Vim editor.
Plug 'scrooloose/nerdtree'

" Lean & mean status/tabline for vim that's light as air.
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Async plugin for Vim/NeoVim to ease the use of ctags/gtags.
Plug 'jsfaint/gen_tags.vim'

" Tagbar
Plug 'preservim/tagbar'

" Supertab is a vim plugin which allows you to use <Tab> for all your insert completion needs
Plug 'ervandew/supertab'

" Insert or delete brackets, parens, quotes in pair.
Plug 'jiangmiao/auto-pairs'

" Moves line up/down
Plug 'matze/vim-move'

" Show indent line
Plug 'Yggdroot/indentLine'

" Show tail space
Plug 'bronson/vim-trailing-whitespace'

" Initialize plugin system
call plug#end()

" Editor configuration
set nu
set cursorcolumn
set cursorline

" tab width
set autoindent
set tabstop=4
set shiftwidth=4

" Replace tab to space when saving file.
autocmd FileType markdown,html,xhtml,xml,xslt,xsd set expandtab
autocmd FileType perl,python,java,javascript set expandtab
autocmd FileType yaml set expandtab shiftwidth=2

" NERDTree
nmap <F5> :NERDTreeToggle<CR>

" Airline
let g:airline_powerline_fonts = 1
let g:airline_theme = 'papercolor'

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

" unicode symbols
let g:airline_symbols.colnr = ' ㏇:'

" Gen_tags
let g:loaded_gentags#ctags = 1

" Tagbar
nmap <F8> :TagbarToggle<CR>

" SuperTab
let g:SuperTabDefaultCompletionType = "<c-n>"

" IndentLine
let g:indentLine_char="│"

