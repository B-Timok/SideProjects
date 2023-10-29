class Task
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}

class Program
{
    static List<Task> tasks = new List<Task>();

    static void Main(string[] args)
    {
        LoadTasksFromFile();
        Console.ForegroundColor = ConsoleColor.Cyan;
        while (true)
        {
            Console.WriteLine("To-Do List Menu:");
            Console.WriteLine("1. Add Task");
            Console.WriteLine("2. View Tasks");
            Console.WriteLine("3. Mark Task as Complete");
            Console.WriteLine("4. Clear Completed Tasks");
            Console.WriteLine("5. Exit\n");

            string choice = Console.ReadLine();

            switch(choice)
            {
                case "1":
                    Console.WriteLine(new string('-', 40));
                    AddTask();
                    break;
                case "2":
                    Console.WriteLine(new string('-', 40));
                    ViewTask();
                    break;
                case "3":
                    Console.WriteLine(new string('-', 40));
                    MarkComplete();
                    break;
                case "4":
                    Console.WriteLine(new string('-', 40));
                    ClearCompletedTasks();
                    break;
                case "5":
                    return;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
                
            }
        }
    }

    static void AddTask()
    {
        Console.WriteLine("Enter task name\n");
        string title = Console.ReadLine();
        tasks.Add(new Task { Title = title, IsCompleted = false});
        Console.WriteLine("\nTask add successfully.\n");
        Console.WriteLine(new string('-', 40));

        SaveTasksToFile();
    }

    static void ViewTask()
    {
        Console.WriteLine("Tasks:\n");
        for (int i = 0; i < tasks.Count; i++)
        {
            Console.WriteLine($"{i + 1}. [{(tasks[i].IsCompleted ? "X" : " ")}] {tasks[i].Title}");
        }
        Console.WriteLine(new string('-', 40));
    }

    static void MarkComplete()
    {
        ViewTask();
        Console.Write("Enter the task number to mark as complete: ");
        if (int.TryParse(Console.ReadLine(), out int taskNumber) && taskNumber >= 1 && taskNumber <= tasks.Count)
        {
            tasks[taskNumber - 1].IsCompleted = true;
            Console.WriteLine("\nTask marked as complete.\n");
            Console.WriteLine(new string('-', 40));

            SaveTasksToFile();
        }
        else
        {
            Console.WriteLine("\nInvalid task number.\n");
        }
    }

    static void ClearCompletedTasks()
    {
        tasks.RemoveAll(task => task.IsCompleted);
        Console.WriteLine("Completed tasks have been cleared.");
        Console.WriteLine(new string('-', 40));
        
        SaveTasksToFile();
    }

    static void SaveTasksToFile()
    {
        using (StreamWriter writer = new StreamWriter("todolist.txt"))
        {
            foreach (Task task in tasks)
            {
                writer.WriteLine($"{task.Title},{task.IsCompleted}");
            }
        }
    }

    static void LoadTasksFromFile()
    {
        if (File.Exists("todolist.txt"))
        {
            // clear current list to load from file
            tasks.Clear();
            using (StreamReader reader = new StreamReader("todolist.txt"))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    string[] parts = line.Split(',');
                    if (parts.Length == 2)
                    {
                        string title = parts[0];
                        bool isCompleted = bool.Parse(parts[1]);
                        tasks.Add(new Task { Title = title, IsCompleted = isCompleted });
                    }
                }
            }
        }
    }
}
