#include "form_profesionales2.h"
#include "ui_form_profesionales2.h"

form_profesionales2::form_profesionales2(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_profesionales2)
{
    ui->setupUi(this);
}

form_profesionales2::~form_profesionales2()
{
    delete ui;
}

void form_profesionales2::on_boton_guardar_clicked()
{

}
