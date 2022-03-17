# Neovim

## Install Neovim on Ubuntu 20.04 LTS

```bash
sudo apt update
sudo apt upgrade

sudo apt install neovim
```

### Vim-plug

```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

Reload init.vim and :PlugInstall to install plugins.
You can use command `:echo stdpath('config')` inside Neovim to find this directory.

1. Run nvim
2. :PluginInstall

## Install Gtags

1. Install Gtags from source code
2. Edit `~/.bashrc`

```bash
export GTAGSCONF=/usr/local/share/gtags/gtags.conf
export GTAGSLABEL=pygments
```

