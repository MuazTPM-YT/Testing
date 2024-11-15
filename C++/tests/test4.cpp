#include <QApplication>
#include <QMainWindow>
#include <QVBoxLayout>
#include <QScrollArea>
#include <QLabel>
#include <QPushButton>
#include <QLineEdit>
#include <QFont>
#include <QDebug>

void collatzconjection(QWidget* parent, QWidget* main_frame, QLineEdit* entry) {
    int integer = entry->text().toInt();
    while (integer != 1) {
        if (integer % 2 != 0) {
            integer = 3 * integer + 1;
            qDebug() << integer;
            QLabel* label = new QLabel(QString::number(integer), main_frame);
            label->setFont(QFont("assets/CalSans-SemiBold.otf", 12));
            label->show();
        }
        else {
            integer /= 2;
            qDebug() << integer;
            QLabel* label = new QLabel(QString::number(integer), main_frame);
            label->setFont(QFont("assets/CalSans-SemiBold.otf", 12));
            label->show();
        }
    }
}

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QMainWindow* window = new QMainWindow();
    window->setWindowTitle("Collatz Conjection");
    window->setGeometry(0, 0, 800, 800);

    QWidget* top_frame = new QWidget(window);
    top_frame->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    window->setCentralWidget(top_frame);

    QScrollArea* scroll_area = new QScrollArea(top_frame);
    scroll_area->setFrameShape(QFrame::NoFrame);
    scroll_area->setWidgetResizable(true);
    top_frame->setLayout(new QVBoxLayout(top_frame));
    top_frame->layout()->addWidget(scroll_area);

    QWidget* main_frame = new QWidget(scroll_area);
    scroll_area->setWidget(main_frame);
    main_frame->setLayout(new QVBoxLayout(main_frame));

    QLineEdit* entry = new QLineEdit(main_frame);
    entry->setPlaceholderText("Number");
    main_frame->layout()->addWidget(entry);

    QPushButton* cc_button = new QPushButton("Generate", main_frame);
    main_frame->layout()->addWidget(cc_button);
    QObject::connect(cc_button, &QPushButton::clicked, [=](){ collatzconjection(scroll_area, main_frame, entry); });

    window->show();
    return app.exec();
}