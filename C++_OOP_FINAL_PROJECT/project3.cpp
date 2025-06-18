#include <iostream>
#include <cstring> // for strcpy, strcmp
using namespace std;

// Define Address struct
struct Address {
    char street[30];
    char city[20];
};

// Abstract base class
class Employee {
protected:
    int id;
    Address* addr;
    float* scores;
    int scoreCount;

public:
    Employee(int id, const char* street, const char* city)
        : id(id), scoreCount(0), scores(nullptr) {
        addr = new Address;
        strcpy(addr->street, street);
        strcpy(addr->city, city);
    }

    virtual ~Employee() {
        delete addr;
        delete[] scores;
    }

    int getId() const { return id; }

    void addScore(float score) {
        float* newScores = new float[scoreCount + 1];
        for (int i = 0; i < scoreCount; ++i) {
            *(newScores + i) = *(scores + i); // pointer arithmetic
        }
        *(newScores + scoreCount) = score;
        delete[] scores;
        scores = newScores;
        ++scoreCount;
    }

    float averageScore() const {
        if (scoreCount == 0) return 0;
        float sum = 0;
        for (int i = 0; i < scoreCount; ++i) {
            sum += *(scores + i); // pointer arithmetic
        }
        return sum / scoreCount;
    }

    virtual float calcSalary() const = 0;

    virtual void printInfo() const {
        cout << "ID: " << id << ", Address: " << addr->street << ", " << addr->city
             << ", Avg Score: " << averageScore() << endl;
    }
};

// Full-time employee
class FullTimeEmployee : public Employee {
    float fixedSalary;
public:
    FullTimeEmployee(int id, const char* street, const char* city, float salary)
        : Employee(id, street, city), fixedSalary(salary) {}

    float calcSalary() const override {
        return fixedSalary;
    }

    void printInfo() const override {
        Employee::printInfo();
        cout << "Type: Full-time, Salary: " << calcSalary() << endl;
    }
};

// Part-time employee
class PartTimeEmployee : public Employee {
    float hourlyRate;
    int hoursWorked;
public:
    PartTimeEmployee(int id, const char* street, const char* city, float rate, int hours)
        : Employee(id, street, city), hourlyRate(rate), hoursWorked(hours) {}

    float calcSalary() const override {
        return hourlyRate * hoursWorked;
    }

    void printInfo() const override {
        Employee::printInfo();
        cout << "Type: Part-time, Salary: " << calcSalary() << endl;
    }
};

// Employee management
class EmployeeManager {
    Employee** staff;
    int count;

public:
    EmployeeManager() : staff(nullptr), count(0) {}

    ~EmployeeManager() {
        for (int i = 0; i < count; ++i)
            delete staff[i];
        delete[] staff;
    }

    void addEmployee(Employee* e) {
        Employee** newStaff = new Employee*[count + 1];
        for (int i = 0; i < count; ++i)
            newStaff[i] = staff[i];
        newStaff[count] = e;
        delete[] staff;
        staff = newStaff;
        ++count;
    }

    void removeEmployee(int id) {
        int index = -1;
        for (int i = 0; i < count; ++i) {
            if (staff[i]->getId() == id) {
                index = i;
                break;
            }
        }
        if (index == -1) {
            cout << "Employee not found.\n";
            return;
        }

        delete staff[index];
        Employee** newStaff = new Employee*[count - 1];
        for (int i = 0, j = 0; i < count; ++i) {
            if (i != index)
                newStaff[j++] = staff[i];
        }
        delete[] staff;
        staff = newStaff;
        --count;
    }

    void printAll() const {
        for (int i = 0; i < count; ++i) {
            staff[i]->printInfo();
            cout << "------------------\n";
        }
    }
};

// Main function to demonstrate
int main() {
    EmployeeManager manager;

    // Create and add employees
    FullTimeEmployee* f1 = new FullTimeEmployee(1, "Main St", "Kigali", 1000.0f);
    f1->addScore(80);
    f1->addScore(90);
    manager.addEmployee(f1);

    PartTimeEmployee* p1 = new PartTimeEmployee(2, "Market Rd", "Huye", 10.0f, 40);
    p1->addScore(75);
    manager.addEmployee(p1);

    manager.printAll();

    // Remove employee by ID
    manager.removeEmployee(1);
    cout << "After removing ID 1:\n";
    manager.printAll();

    return 0;
}
