tasks = []

def addTask():
     task = input("PLease enter a task :")
     tasks.append(task)
     print(f"Task '{task}' added to the  list.")

def listTasks():
    if not tasks:
         print("There are no task currently.")
    else:
         print("current Task:")
         for index, task in enumerate(tasks):
              print(f"Task #{index}. {task}")
              
          
     
def deleteTask():
     listTasks()
     try:
        taskToDelete= int(input("choose the task you want to delete :"))
        if taskToDelete>=0 and taskToDelete < len(tasks):
             tasks.pop(taskToDelete)
             print(f"Task #{taskToDelete} has been removed.")
        else:
             print(f"Task #{taskToDelete} was not found.")
     except:
          print("Invalid input.")

          


if __name__=="__main__":
    print("Welcome to the To_do list :")
    while True:
         print("\n")
         print("Please select one of the following options")
         print("______________________________________________")
         print("1. Add a new task")
         print("2. List tasks")
         print("3. Delete a task")
         print("4. Exit")

         choice = input("Enter your choice :")

         if(choice =="1"):
              addTask()
         elif(choice =="2"):
              listTasks()
         elif(choice =="3"):
              deleteTask()
         elif(choice =="4"):
              break
         else:
              print("Invalid input. please try again")
    
    print("App closed")

                   

        
        
         
