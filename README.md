> To have no errors <br>
> Would be life without meaning <br>
> No struggle, no joy <br>
> ~ (Brian M. Porter)


# haiku-errors

Just `import haiku_errors` to print a haiku whenever exception is not handled:

```console
$ python -c "import haiku_errors; raise SystemError"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
SystemError
    
    Something has gone wrong.
    Format your disk, because this
    Error won't help you.
    ~ (Cheryl Walker)
    
```

One liner example without explicit `raise`:

```console
$ python3 -c "import haiku_errors; f = lambda: f(); f()"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
LookupError
    
    The ten thousand things,
    How long do any persist?
    Netscape, too, has gone.
    ~ (Jason Willoughby)
    
```

To install run:

    $ pip install haiku-errors
