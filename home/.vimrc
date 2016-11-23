call plug#begin()
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'vim-airline/vim-airline'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'vim-scripts/taglist.vim'
Plug 'tpope/vim-sensible'
Plug 'sickill/vim-monokai'
call plug#end()

set number

if has('gui_running')
  set guifont=PragmataPro\ for\ Powerline:h10
  " colorscheme evening
  colorscheme monokai
  set guioptions-=T  " no toolbar
endif

" Normal Mode Maps
nmap <Space>ft :NERDTreeToggle<CR>
nmap <Space>p <C-p>

" Insert Mode Maps
imap jj <Esc>
imap fd <Esc>
