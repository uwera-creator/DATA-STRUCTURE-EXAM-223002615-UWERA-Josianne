#include <iostream>
#include <vector> // Vector added
using namespace std;

// Base Class
class Account {
protected:
    int accNum;
    double balance;
public:
    Account(int num = 0, double bal = 0) {
        accNum = num;
        balance = bal;
    }

    void deposit(double amt) {
        balance += amt;
        cout << "Deposited: $" << amt << endl;
    }

    void withdraw(double amt) {
        if (amt <= balance) {
            balance -= amt;
            cout << "Withdrawn: $" << amt << endl;
        } else {
            cout << "Insufficient funds!" << endl;
        }
    }

    virtual void display() {
        cout << "Account #" << accNum << " - Balance: $" << balance << endl;
    }

    virtual ~Account() {} // Virtual destructor for cleanup
};

// Single Inheritance
class Savings : public Account {
public:
    Savings(int num, double bal) : Account(num, bal) {}
};

// Hierarchical Inheritance
class Current : public Account {
public:
    Current(int num, double bal) : Account(num, bal) {}
};

// Multilevel Inheritance
class InternationalSavings : public Savings {
public:
    InternationalSavings(int num, double bal) : Savings(num, bal) {}

    void showAccess() {
        cout << "Online Access Enabled" << endl;
    }

    void display() {
        Account::display();
        showAccess();
    }
};

// Additional feature class (no inheritance from Account)
class LoanFeatures {
public:
    void showLoanInfo() {
        cout << "Loan Services Available" << endl;
    }
};

// Another feature class
class SavingsFeatures {
public:
    void showSavingsFeature() {
        cout << "Interest Accrual Enabled" << endl;
    }
};

// Hybrid Inheritance class (Multiple Inheritance)
class BankApp : public SavingsFeatures, public LoanFeatures {
public:
    void showAppFeatures() {
        showLoanInfo(); // from LoanFeatures
        showSavingsFeature(); // from SavingsFeatures
        cout << "Mobile Banking Enabled" << endl;
    }
};

int main() {
    // Create a vector to store Account pointers
    vector<Account*> accounts;

    // Create account objects dynamically
    Account* s = new Savings(101, 1000);
    Account* c = new Current(102, 500);
    Account* i = new InternationalSavings(103, 1200);

    // Add to vector
    accounts.push_back(s);
    accounts.push_back(c);
    accounts.push_back(i);

    // Perform operations
    s->deposit(300);
    s->withdraw(100);

    // Display all accounts using polymorphism
    cout << "\n--- Account Information ---\n";
    for (int j = 0; j < accounts.size(); j++) {
        accounts[j]->display();
    }

    // Show hybrid app features
    cout << "\n--- Bank App Features (Hybrid Inheritance) ---\n";
    BankApp app;
    app.showAppFeatures();

    // Cleanup memory
    for (int j = 0; j < accounts.size(); j++) {
        delete accounts[j];
    }

    return 0;
}
