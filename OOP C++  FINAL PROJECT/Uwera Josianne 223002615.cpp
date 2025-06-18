#include <cstdio>
#include <cstring>

// Date structure
struct Date {
    int day;
    int month;
    int year;
};

// Attendance structure
struct AttendanceRec {
    char studentID[10];
    char studentName[20];
    Date* date;
    bool present;
};

// Report base interface
class ReportInterface {
public:
    virtual ~ReportInterface() {}
    virtual void generate(const AttendanceRec* recs, int n) = 0;
};

// Daily Attendance Report
class DailyAttendanceReport : public ReportInterface {
public:
    void generate(const AttendanceRec* recs, int n) {
        printf("=========== DAILY ATTENDANCE REPORT ===========\n");
        int presentCount = 0;

        for (int i = 0; i < n; ++i) {
            printf("Student: %-10s (%s) | Date: %02d/%02d/%4d | Status: %s\n",
                   recs[i].studentName,
                   recs[i].studentID,
                   recs[i].date->day,
                   recs[i].date->month,
                   recs[i].date->year,
                   recs[i].present ? "Present" : "Absent");
            if (recs[i].present) presentCount++;
        }

        printf("Total Present: %d out of %d students\n", presentCount, n);
        printf("===============================================\n\n");
    }
};

// Trend Attendance Report
class TrendAttendanceReport : public ReportInterface {
public:
    void generate(const AttendanceRec* recs, int n) {
        printf("=========== TREND ATTENDANCE REPORT ===========\n");

        if (n < 2) {
            printf("Not enough data to determine trend.\n");
            printf("===============================================\n\n");
            return;
        }

        // Show first and last entries
        printf("First Entry : %s (%s) - %s\n",
               recs[0].studentName, recs[0].studentID,
               recs[0].present ? "Present" : "Absent");

        printf("Last Entry  : %s (%s) - %s\n",
               recs[n - 1].studentName, recs[n - 1].studentID,
               recs[n - 1].present ? "Present" : "Absent");

        // Calculate presence ratio
        int presentCount = 0;
        for (int i = 0; i < n; ++i) {
            if (recs[i].present) presentCount++;
        }

        double ratio = (double)presentCount / n * 100;
        printf("Presence Ratio: %.2f%%\n", ratio);

        // Interpret trend
        if (ratio >= 75.0)
            printf("Trend: Good (= 75%% presence)\n");
        else if (ratio >= 50.0)
            printf("Trend: Moderate (50%% – 74%% presence)\n");
        else
            printf("Trend: Poor (< 50%% presence)\n");

        printf("===============================================\n\n");
    }
};

// Attendance Manager
class AttendanceManager {
private:
    AttendanceRec* recs;
    int size;

public:
    AttendanceManager() {
        recs = NULL;
        size = 0;
    }

    ~AttendanceManager() {
        for (int i = 0; i < size; ++i) {
            delete recs[i].date;
        }
        delete[] recs;
    }

    void addAttendance(const AttendanceRec& newRec) {
        AttendanceRec* temp = new AttendanceRec[size + 1];
        for (int i = 0; i < size; ++i) {
            temp[i] = recs[i];
        }

        temp[size].date = new Date;
        *temp[size].date = *newRec.date;
        std::strcpy(temp[size].studentID, newRec.studentID);
        std::strcpy(temp[size].studentName, newRec.studentName);
        temp[size].present = newRec.present;

        delete[] recs;
        recs = temp;
        size++;
    }

    void removeAttendance(int index) {
        if (index < 0 || index >= size) {
            printf("Invalid index.\n");
            return;
        }

        delete recs[index].date;

        AttendanceRec* temp = new AttendanceRec[size - 1];
        int j = 0;
        for (int i = 0; i < size; ++i) {
            if (i != index) {
                temp[j] = recs[i];
                temp[j].date = new Date;
                *temp[j].date = *recs[i].date;
                j++;
            }
        }

        delete[] recs;
        recs = temp;
        size--;
    }

    AttendanceRec* getRecords() const { return recs; }
    int getSize() const { return size; }
};

// Main function
int main() {
    AttendanceManager manager;

    const char* names[] = { "Uwera", "Josianne", "Arthur","Darren","Talent" };
    bool presentFlags[] = { true, false, true };
    int days[] = {1, 2, 3};

    for (int i = 0; i < 5; ++i) {
        AttendanceRec rec;
        std::sprintf(rec.studentID, "S00%d", i + 1);
        std::strcpy(rec.studentName, names[i]);

        rec.date = new Date;
        rec.date->day = days[i];
        rec.date->month = 6;
        rec.date->year = 2025;

        rec.present = presentFlags[i];
        manager.addAttendance(rec);
    }

    // Reports
    ReportInterface* reports[2];
    reports[0] = new DailyAttendanceReport();
    reports[1] = new TrendAttendanceReport();

    // Initial Reports
    for (int i = 0; i < 2; ++i) {
        reports[i]->generate(manager.getRecords(), manager.getSize());
    }

    // Remove Bob (index 1)
    manager.removeAttendance(1);

    printf(">>> After Removing Index 1 :\n\n");

    for (int i = 0; i < 2; ++i) {
        reports[i]->generate(manager.getRecords(), manager.getSize());
    }

    // Clean up
    for (int i = 0; i < 2; ++i) {
        delete reports[i];
    }

    return 0;
}

