"Port from Swaroop's Vimrc file
" Maintainer: swaroop@swaroopch.com

"" Vim, not Vi.
" This must be first, because it changes other options as a side effect.
set nocompatible
" required! by vundle
filetype off

"" Vundle
"" See :help vundle for more details
set runtimepath+=~/.vim/bundle/vundle/
call vundle#rc()


" let Vundle manage Vundle
" required! by vundle
Bundle 'gmarik/vundle'
Bundle 'SuperTab'
Bundle 'javacomplete'

" Git Repos by http://vim-scripts.org ( get names from " https://github.com/vim-scripts/following )
"Bundle 'perlomni.vim'


"" General Settings

" Enable syntax highlighting.
syntax on

" Line endings should be Unix-style unless the file is from someone else.
set fileformat=unix
au BufNewFile * set fileformat=unix

" Automatically indent when adding a curly bracket, etc.
" required! by vundle
filetype plugin indent on
set autoindent
set smartindent

" Tabs converted to 4 spaces
set shiftwidth=4
set tabstop=4
set expandtab
set smarttab
set backspace=indent,eol,start

" Disable the F1 help key
map <F1> <Esc>
imap <F1> <Esc>

" Highlight current line
set cursorline

" Use UTF-8
set encoding=utf-8

" Show line number, cursor position.
set ruler

" Display incomplete commands.
set showcmd

" Search as you type.
set incsearch

" Ignore case while searching
set ignorecase

" Make /g flag default when doing :s
set gdefault

" Show autocomplete menus
set wildmenu

" Show editing mode
set showmode

" Ignore certain filetypes when doing filename completion
set wildignore=*.sw*,*.pyc,*.bak

" Show matching brackets
set showmatch

" Bracket blinking
set matchtime=2

" Split new window below current one
set splitbelow

" Error bells are displayed visually.
set visualbell

" Automatically read files which have been changed outside of Vim, if we
" haven't changed it already.
set autoread

" Disable highlighting after search. Too distracting.
set nohlsearch

" To save, ctrl-s.
nmap <c-s> :w<CR>
imap <c-s> <Esc>:w<CR>a

" Reformatting options. See `:help fo-table`
set formatoptions+=lnor1

" Disable spellcheck by default
set nospell
autocmd BufRead,BufNewFile * setlocal nospell
" To enable again, use:
" setlocal spell spelllang=en_us

" See `:help key-notation`
" Shortcuts for moving between tabs
" Alt-j to move to the tab to the left
noremap <A-j> :tabN<CR>
" Alt-k to move to the tab to the right
noremap <A-k> :tabn<CR>

" Shortcut for moving between windows
nnoremap <c-j> :wincmd w<CR>

" Shortcut to insert date
inoremap <F5> <C-R>=strftime("%a, %d %b %Y")<CR>


" Python omni-completion
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
" Close the preview window
" let g:SuperTabClosePreviewOnPopupClose = 1
autocmd CursorMovedI * if pumvisible() == 0|pclose|endif
autocmd InsertLeave * if pumvisible() == 0|pclose|endif

" Perl omni-completion
autocmd FileType perl setlocal omnifunc=PerlComplete

" Java omni-completion
autocmd FileType java setlocal omnifunc=javacomplete#Complete

"" Bundle-specific configurations
" With SuperTab installed, press Tab instead of Ctrl-X then Ctrl-O
let g:SuperTabDefaultCompletionType = "<c-x><c-o>"

" Let SuperTab decide which completion mode to use
"let g:SuperTabDefaultCompletionType = "context"
