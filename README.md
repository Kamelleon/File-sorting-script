# PySort
A small program that sort files by adding them to specific folder with the name of extension


# Instructions
- __Minimum Python 3.7.5 required__
- Place script in location where you want to sort files
- Run it

# Add your own extension to script

Additionally you can modify this script to sort only files with extension specified by you.
Just add line of code:
```python
if __name__ == '__main__':
  sortfiles('.extension')
```
And change 'extension' with the name of your extension for e.g.
```python
if __name__ == '__main__':
  sortfiles('.mp3')
```
