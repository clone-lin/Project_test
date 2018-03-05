# Vim 8
[Ubuntu]
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim

# Vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# Install plugins
1. Run vim
2. :PluginInstall

# YouCompleteMe
cd ~/.vim/bundle/YouCompleteMe
./install.sh --clang-completer

