1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```
branch: master

commits:

commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)

branch: math

commits: 

commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:13:48 2019 -0700

    Adding some more knowledge to the function

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)
```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)
       
First, a commit was added to the master branch. In the math branch, a separate commit was created and then merged with the master branch. From there, two more commits were added to the master branch.

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
Compared to the master branch, it appears that nine lines were removed from and one line was added to b/A.py, and one line was added to b/B.py.

diff --git a/A.py b/A.py
index 0afa98c..dc1e9bd 100644
--- a/A.py
+++ b/A.py
@@ -1,11 +1,3 @@
 #this is just an example, do not freak out
 def calculate_this(operator, num1, num2):
-   if operator == 'sum':
-      print num1 + num2
-      print 'That was easy buddy'
-   else:
-      if operator == 'subtraction':
-         print num1 - num2
-         print 'I could handle that...'
-      else:
-         print 'my knowledge is limited'
+   print 'my knowledge is limited'
diff --git a/B.py b/B.py
index e69de29..c63f94c 100644
--- a/B.py
+++ b/B.py
@@ -0,0 +1 @@
+# Another file that will receive a line of code... at least.

```

4. Write a command sequence to merge the non-master branch into `master`.

```
git checkout master
git merge math

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
git checkout master
git branch math
git checkout math
```
   
6. Edit B.py adding the following source code below the content you have there.
```
print 'I know math, look:'
print 2+2
(added above lines to B.py file)
```

7. Write a command (or sequence) to commit your changes.
```
git commit -a -m 'for Q7'
```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
git checkout master
(added: print 'hello world!' to B.py)
git commit -a -m 'for Q8'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
git merge math

Gives me the following message: 
"CONFLICT (content): Merge conflict in B.py
Automatic merge failed; fix conflicts and then commit the result."

This occurred because different changes were made to the same file in separate branches by different people.
```
   
10. Write a set of commands to abort the merge.
```
git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```
I changed the B.py files in both branches so that they matched, committed the chaanges using git commit -a -m, and then merged the branches using git merge math.

```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
git checkout master
git merge math

```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```
should i have donw this in git?

```
