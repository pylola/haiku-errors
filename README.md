> To have no errors
> Would be life without meaning
> No struggle, no joy
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
$ python -c "import haiku_errors; raise SystemError"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
SystemError
    
    Something has gone wrong.
    Format your disk, because this
    Error won't help you.
    ~ (Cheryl Walker)
    
```

To install run:

    $ pip install haiku-errors