---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(launch/thebe)=
# Introduction to the Command Line

This module is designed to introduce you to the basic commands and tools needed to run your first scientific computing application. We will start with basic commands to execute in a Unix Shell.

The command line is the text-based interface for the computer's operating system as a powerful alternative to the click-pointer interaction. It is a program that takes in commands and passes them on to the computer's operating system to run. For example, through the command line, you can create or delete files and edit their content. The advantage of using the command line is its power. You can run programs, write scripts to automate common tasks, and combine simple commands to handle difficult tasks. By the end of this session, you should be able to navigate, access, and modify files and folders on your computer - all without a mouse!

## Command Line Basics

In the terminal, the first thing you see is an **$** symbol. This is called a *shell prompt*, and whenever you see it, it means that the terminal or shell is ready to accepy a command. But what is a command? A *command* is a text-based instruction to the computer to perform a specific task. For example, one of the commands you will use on a daily basis is *ls*.

When you type *ls*, the command line looks at the directory you are in, and "lists" all the files and directories inside of it. You can try it now for yourself!

```{code-cell} ipython3
%%bash
ls
```

## Command Line Navigation 
When using the command line, we refer to folders as *directories*. Files and directories on your computer are organized into a *filesystem*. The *filesystem* is the tree structure organization of the files and directorates in your computer. Think about it as the *Mac Finder* or *Windows Explorer* without the ability to access directories and files with a click. 

- The top directory in the filesystem is the *root* directory.

- In this nested structure, we refer to directories as *parents* and *childs* according to their position in the tree. The top directory is the *parent* of any other file or directory in the system. We are now going to explore a few basic commands to navigate your computer's *filesystem*. 

The next command we are going to explore is *pwd*. It stands for *print working directory* and it indeed, outputs the name of the directory you are currently in.

```{code-cell} ipython3
%%bash
pwd
```
Our next command is *cd*, which stands for *change directory*.

```{code-cell} ipython3
%%bash
cd <folder-name>
```

*cd* also allows you to navigate deeper into the *filesystem* without having to use it twice. For example, if you want to access *Folder1* inside *FolderA*, you can type

```{code-cell} ipython3
%%bash
cd FolderA/Folder1/
```
A useful tip is to use the *tab* key to autocomplete the name of a given file or folder. It will probably won't work on the web browser environment but you can try it on your Unix terminal. Also, let's say you want to access *Folder2* inside *FolderA* while you are already on *Folder1*, you can go back one level by typyng ../

```{code-cell} ipython3
%%bash
cd ../Folder2/
```

## Editing the filesystem

You can create a directory by typing

```{code-cell} ipython3
%%bash
mkdir <your-name>
```
to create a file, you can simply do

```{code-cell} ipython3
%%bash
touch <filename>
```

## Viewing and changing the file system

The shell command *cp* is used to copy files or directories. The basic argument structure is *cp source destination*, where the *source* is the file/directory to copy to the *destination* file/directory.

```{code-cell} ipython3
%%bash
cp file1 file1_copy
cp file1 file2 destination_folder
```

The shell command *mv* is used to move a file into a directory. Use *mv* with the source file as the first argument and the destination directory as the second argument.

```{code-cell} ipython3
%%bash
mv file.txt myFolder/
```

The shell command *rm* is used to delete files and directories. The *-r* flag deletes a directory and all of its files and directories (*rm -r*).

```{code-cell} ipython3
%%bash
rm -r bad_selfies
```
The shell command *ls* is used to list the contents in a directory. It can be combined with the following command options:
- *-a*: lists all contents, including hidden files and directories.
- *-l*: lists all contents, in long format.
- *-t*: lists all contents, by the time they were last modified.

## Command line redirection
On a command line, *redirection* is the process of using the input/output of a file or command to use it as an input for another file. Redirection can be done by using the operators *>* and *>>*.

```{code-cell} ipython3
%%bash
ls > directories_list.txt
ls >> directories_list.txt
```

The *>* symbol is used to redirect output by taking the output from the command on the left and passing as input to the file on the right. 

```{code-cell} ipython3
%%bash
echo "Hola" > hola.txt
```

The shell command *cat* displays the contents of one or more files to the terminal.

```{code-cell} ipython3
%%bash
cat poem.txt
```

if you just want to print the first or last few lines of a file, you can use *head* or *tail*:

```{code-cell} ipython3
%%bash
head poem.txt
tail poem.txt
```

The *>>* shell command is used to redirect the standard output of the command line on the left and append (add) it to the end of the file on the right.

```{code-cell} ipython3
%%bash
#This command will append "Hello World!" to greetings.txt
echo "Hello World!" >> greetings.txt
```

The *|* command is called a *pipe*. It is used to pipe, or transfer, the standard output from the command on its left into the standard input of the command on its right.

```{code-cell} ipython3
%%bash
# First, echo "Hello World" will send Hello World to the standard output.
# Next, pipe | will transfer the standard output to the next command's standard input.
# Finally, wc -w will count the number of words from its standard input, which is 2.
echo "Hello World" | wc -w
```
The shell command *grep* is used to search files for lines that match a pattern and returns the results. Various options can be specified along with the *grep* command to specify the search.

```{code-cell} ipython3
%%bash
grep 'Andrea' names.txt
```
- The shell *grep* command searches files for a particular pattern. Adding the *-i* option can be used to search files for lines that match a pattern, case sensitive, and returns the results.
- The *-R* option searches all files in a directory, including its subdirectories, and outputs filenames and lines containing matched results.

Finally, you can run bash code on your terminal, to execute a specific task. For example,

```{code-cell} ipython3
%%bash
for i in a b c;
do
echo $i
done
```
