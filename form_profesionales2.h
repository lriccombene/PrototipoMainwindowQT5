#ifndef FORM_PROFESIONALES2_H
#define FORM_PROFESIONALES2_H

#include <QDialog>

namespace Ui {
class form_profesionales2;
}

class form_profesionales2 : public QDialog
{
    Q_OBJECT

public:
    explicit form_profesionales2(QWidget *parent = 0);
    ~form_profesionales2();

private slots:
    void on_boton_guardar_clicked();

private:
    Ui::form_profesionales2 *ui;
};

#endif // FORM_PROFESIONALES2_H
