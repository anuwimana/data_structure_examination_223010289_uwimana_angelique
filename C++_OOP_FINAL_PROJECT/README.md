Employee Management System – C++

Project Title
Employee Management System

Task Overview
A C++ program to manage full-time and part-time employees using OOP concepts:

Inheritance and Polymorphism

Abstract Classes

Dynamic Memory and Pointer Arithmetic

Each employee has:

An address (street and city)

A dynamic array of performance scores

A polymorphic method to calculate salary

Key Features
struct Address with dynamic allocation

Abstract class Employee with:

ID, address, scores array

Pure virtual calcSalary()

Average score function

Derived classes:

FullTimeEmployee: Fixed salary

PartTimeEmployee: Hourly rate × hours worked

Dynamic array Employee** staff for storing employees

Memory managed using new and delete[]

Sample Code Snippet
cpp
Copy
Edit
struct Address {
    char street[30];
    char city[20];
};

class Employee {
protected:
    int id;
    Address* addr;
    float* scores;
    int scoreCount;

public:
    Employee(int id, const char* street, const char* city) {
        this->id = id;
        addr = new Address;
        strcpy(addr->street, street);
        strcpy(addr->city, city);
        scores = nullptr;
        scoreCount = 0;
    }

    virtual float calcSalary() const = 0;
};
