# Chapter 4: Working with lists

This chapter introduces loops! And also explains how indentation is used in Python, 
and warns of the common errors made when indenting code, too many or too few indents. 
List comprehensions make an appearance as do Tuples.

The chapter concludes with some information about coding style, which is often overlooked when learning but
is then in dire need of correcting as you develop larger and more complex projects. Python has a very active and 
established community at this point in time (2024) and so already have some established conventions and best practices
for what constitutes "good code". In short "Readability Rules"

The editor I am using, PyCharm, basically handles that for me which is great ☺

```python
# Code Covered
my_list = [1,2,3,4,5]
for item in my_list:
    print(item)

print([number * 10 for number in range(0,11)])
sum([min(my_list),max(my_list)])

new_name_for_my_list = my_list
copy_to_work_on = my_list[:]
hard_coded_value = (256)
hard_coded_value = "aaaaa"
```