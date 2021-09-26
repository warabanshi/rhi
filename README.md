# rhi remote history

`rhi` is a command that saving/retrieving commands to/from remote server.

How do you save commands it's not frequently used but sometime it will be required or it's too long to re-enter it. It is awkward but, as for me, I save it to a memo file and copy & paste it to CLI when I require it. (Let me know if there are other neat things to do)

Of course, to search hisotry I use `ctrl + r` also but it depends `history` of the shell process so, basically, newly added histories aren't shared among multiple ssh connections even if those all are connecting same server. In addition to it, commands you require may be overwritten when close the multiple connections depending on closing order. And, as you know, there's a upper limit that history can have it.

`rhi` release us from these frustrations by saving commands for server. `rhi` command saving those to server side application [rhi-server](https://github.com/warabanshi/rhi-server).

## Usage

### Adding a command

Add a last command of `history` except `history` itself at the tail of the result.

```
$ history | rhi -a
```

Add a numbered history in `history` command
```
$ history | rhi -a -n 10  # add a command row number 10
```

Add a command with message
```
$ history | rhi -a -m 'This is sample message'
```

### Getting saved commands

Get all saved commands

```
$ rhi
```

Get a particular command
```
$ rhi -n 10  # get a command row number 10 of saved commands
```

### Running a commnad

Run a retrieved command 

```
$ rhi -r 15  # run a command row number 15 of saved commands
```

### Flushing saved commands

Flush all saved commands
```
$ rhi -f
```

## Running tests

`run_test.sh` file runs `mypy`, `flake8` and `pytest`. These expect it will be run under poetry venv.

```
$ . .venv/bin/activate
(.venv) $ ./run_test.sh
```
