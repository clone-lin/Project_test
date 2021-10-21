# Vim 8
[Ubuntu]
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim

# Vundle
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# Reload .vimrc and :PlugInstall to install plugins.
1. Run vim
2. :PluginInstall

# YouCompleteMe
cd ~/.vim/bundle/YouCompleteMe
./install.sh --clang-completer

