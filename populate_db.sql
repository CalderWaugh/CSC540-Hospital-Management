DROP DATABASE IF EXISTS medclinic;
CREATE DATABASE medclinic;
USE medclinic;

drop table if exists patient;
Create table Patient (
patient_id int (10),
first_name varchar (20),
last_name varchar (20),
date_of_birth date,
insurance_id int (20),
phone_num varchar (20),
patient_address varchar (30),
ssn int (15),
primary key (patient_id)
);

insert into patient
Values ( 11, 'Rodger', 'Clemens','1975-06-23',234221,8603342344,'123 Charter Road', 982331234);

insert into patient
Values ( 13, 'Tom', 'Brady','1979-01-27',288321,8602248744,'234 Patriots Road', 332135678);

insert into patient
Values ( 15, 'Brett', 'Farve','1981-09-12',288555,8601338464,'274 Packers Road', 543133563);

insert into patient
Values ( 18, 'Aaron', 'Judge','1982-11-22',298433,8603312457,'574 Yankee Road', 345331365);

insert into patient
Values ( 10, 'Scarlet', 'Johansen','1983-02-12',134432,8603217757,'675 Melrose Drive', 554331990);

insert into patient
Values ( 20, 'Meghan', 'Fox','1984-10-25',216634,2133332257,'699 Melrose Drive', 443221642);

insert into patient
Values ( 23, 'Amanda', 'Larusso','1980-02-11',612654,6123331167,'788 Sunset Drive', 344112642);

insert into patient
Values ( 26, 'Daniel', 'Larusso','1981-06-21',992654,6125532167,'788 Sunset Drive', 541133412);

insert into patient
Values ( 29, 'Mel', 'Gibson','1972-01-12',192123,3217541267,'741 Rocky Road Drive', 531124121);

insert into patient
Values ( 31, 'Eddy', 'Money','1974-02-19',432765,8547543244,'123 Paradise Drive', 678812432);

insert into patient
Values ( 36, 'Freddie', 'Mercury','1975-01-27',982123,4341549900,'567 Bohemian Drive', 712909322);

insert into patient values 
(38,'Greg','Lank','1991-02-13',456780,4756789087,'690 Columbus Avenue',123456751);
insert into patient values
 (40,'Bob','Bousy','1929-03-13',678543,4756543289,'56 Rodeo Planes',234789065);
insert into patient values
 (42,'Kelly','Under','1997-08-21',456055,4756907813,'760 Mckinley Street',567903298);
insert into patient values
 (44,'Robert','James','1998-04-11',356709,4567890348,'560 Mchine Avenue',098765409);
insert into patient values
 (46,'Jaime','Cedron','1935-07-28',456732,2034567825,'56 Green Avenue',056980754);
Insert into patient values 
(48,'Bear','Hines','1978-05-19',290132,5789808765,'45 Columbus Street',098076579);
Insert into patient values
 (50,'James','Berel','1991-02-01',342287,2034757474,'180 Hines Drive',087900985);
Insert into patient values 
(52,'Bre','Brown','1992-03-15',432764,2034573290,'18 Bear Owen Street',089900978);
insert into patient values
 (54,'Bre','Benji','1993-03-16',234531,2033323456,'12 Bear Road',03446743);
Insert into patient values 
(56,'George','Broe','1995-09-15',345618,2034567831,'11 Roe Street',098765489);
Insert into patient values 
(58,'Mike','Jones','1997-09-24',367908,2034588901,'10 Ben Street',034567908);
Insert into patient values
 (60,'Jen','Jenny','2000-01-01',098760,2034320112,'1209 Robe Avenue',067890547);
insert into patient values
 (62,'Nie','Page','2001-01-28',098321,2034569809,'1301 Rodeo Planes',078954312);
insert into patient values
 (63,'Greg','Brooks','2003-09-13',056780,2034328907,'1302 Ben Street',098765490);
insert into patient values
 (64,'Tom','Mario','2005-04-22',013908,2034321212,'13 Hines Drive',043567801);
insert into patient values
 (66,'Kim','Kardashian','1978-09-11',024567,2034020202,'14 Rose Avenue',098765490);
insert into patient values
 (68,'Kim','Benjamin','1902-03-12',034908,2030980091,'56 Newman Street',097569009);
insert into patient values
 (70,'Him','Himothy','1974-09-10',021908,2034567098,'7 Ben Road',093090021);
Insert into patient values
 (72,'Geez','Kimmy','1932-01-21',031908,2034750981,'81 Gregory Circle',044966077);
Insert into patient values
 (74,'Harry','Jay','1997-04-09',031290,4744390878,'181 James Street',098090876);
Insert into patient values
 (76,'Corey','Leah','1998-04-11',030290,4744790878,'109 James Street',006090876);



drop table if exists medication;
create table Medication (
medication_id int (10),
medication_name varchar (25),
generic varchar (25),
dosage varchar (20),
primary key (medication_id)
);


insert into medication
values (2341,'Penicillin','Liapro','50MG');

insert into medication
values (4321,'Vicodin','thiamin','5MG');

insert into medication
values (7321,'Tylenol','Thorazin','10MG');

insert into medication
values (8113,'Advil','Morthil','12MG');

insert into medication
values (3391,'Lexapro','Nilthin','15MG');

insert into medication
values (3991,'Amlodipine','Norvasc','20MG');
insert into medication
values (3274,'Prednisone','Deltasone','35MG');

insert into medication
values (1204,'Amoxicillin','Amoxil','38MG');


insert into medication
values (1994,'Lisinopril','Zestril','50MG');

insert into medication
values (3014,'Levothyroxine','Synthroid','50MG');

insert into medication
values (3923,'Virthrol','Teranord','57MG');


CREATE TABLE Pharmacy (
pharmacy_id int (10),
name varchar(25),
address varchar (25),
primary key (pharmacy_id)
);

insert into Pharmacy
values (1234,'CVS','174 SunDale Avenue');

insert into Pharmacy
values (3324,'CVS','74 Farmington Avenue');

insert into Pharmacy
values (1024,'Target','177 Ferndale Street');
insert into Pharmacy
values (1908,'Walmart','77 Stanley Street');

insert into Pharmacy
values (1998,'RiteAid','454 Robin Street');

insert into Pharmacy
values (3246,'Walgreens','12 Beck Road');

insert into Pharmacy
values (2364,'Target','34 Roberts Road');

insert into Pharmacy
values (3214,'CVS','554 Clark Street');

insert into Pharmacy
values (1204,'Walmart','67 Corbin Street');

insert into Pharmacy
values (1999,'RiteAid','674 Newington Avenue');

insert into Pharmacy
values (6419,'RiteAid','246 Dale Avenue');




create table Prescription (
prescription_id int auto_increment,
pharmacy_id int,
medication_id int,
patient_id int,
date_prescribed date,
current_diagnosis_severity varchar(20),
refills int,
primary key (prescription_id),
foreign key (pharmacy_id) references Pharmacy(pharmacy_id),
foreign key (patient_id) references Patient(patient_id),
foreign key (medication_id) references Medication(medication_id)
);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (1234, 2341,11, '2021-01-20',5,3);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (3324, 4321,13, '2022-02-23',4,1);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (1024, 7321,15, '2022-03-09',3,2);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (1908, 8113,18, '2022-04-11',6,3);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (1998, 3391,10, '2021-11-21',4,3);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (3246, 3991,20, '2021-10-11',6,2);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (2364, 3274,23, '2022-05-23',3,1);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (3214, 1204,26, '2022-06-13',7,2);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (1204, 1994,29, '2022-01-23',7,1);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (1999, 3014,31, '2021-11-29',1,4);

insert into Prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills)
values (6419, 3923,36, '2022-10-11',8,5);

insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(1234,2341,38,'2022-11-29',7,2);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(3324,3014,40,'2022-11-30',2,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(1024,1994,42,'2022-11-29',5,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values
(1999,3923,44,'2022-11-30',9,4);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values
(1908,3991,46,'2022-12-01',1,0);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(3246,4321,48,'2022-11-29',2,0);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values
(3214,3923,50,'2022-11-29',3,0);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(1204,3014,52,'2022-11-30',4,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(2364,3274,54,'2022-11-29',9,3);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(1024,3991,56,'2022-12-01',8,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values
(1999,1994,58,'2022-11-30',7,2);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(6419,7321,60,'2022-11-29',5,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(2364,8113,62,'2022-11-29',6,3);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(1234,3923,63,'2022-12-01',9,5);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(2364,1994,64,'2022-11-30',8,3);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(1998,3014,66,'2022-11-29',5,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values
(6419,1994,68,'2022-11-30',8,1);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(3214,3274,70,'2022-12-01',7,3);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values
(1204,3991,72,'2022-12-01',9,7);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(3246,3274,74,'2022-11-29',5,2);
insert into prescription (pharmacy_id, medication_id, patient_id, date_prescribed, current_diagnosis_severity, refills) values 
(2364,3991,76,'2022-11-29',6,1);





drop table if exists bill;
Create table Bill (
Bill_ID int,
total_cost int,
Owed int,
Primary Key (Bill_ID)
);

drop table if exists hospital;
Create Table Hospital (
Hospital_ID int,
Hospital_name varchar (50),
Available_rooms int,
rooms_in_use int,
Primary Key (Hospital_ID)
);

drop table if exists department;
Create table Department(
Department_id INT,
hospital_name VARCHAR (20),
department VARCHAR (20),
Primary key (department_id) 
); 

INSERT INTO department
VALUES
(1, 'Yale New Haven', 'Cardiology'),
(2, 'Yale New Haven', 'Emergency Department'),
(3, 'Yale New Haven', 'Oncology'),
(4, 'Yale New Haven','MedSurge'),
(5, 'Yale New Haven', 'Psych'),
(6, 'Yale New Haven', 'Neurology'),
(7, 'Physician One', 'General'),
(8, 'Yale New Haven', 'Radiology');

DROP TABLE IF EXISTS doctor;
CREATE TABLE doctor(
	doctor_employee_id INT,
    department_id INT,
    name VARCHAR(30),
    position VARCHAR(30),
    registered BOOLEAN,
    password VARCHAR(200),
    PRIMARY KEY(doctor_employee_id),
    FOREIGN KEY(department_id) references Department(department_id)
);

#pssword key:Rob Jenkins= Rjenkins
insert into doctor values (1234,1,'Rob Jenkins','Lead cardiologist',True,'pbkdf2:sha256:260000$i5qDMxkQI3EyuXZc$f14af114e33e09904248cc647abc84ec808bebc1fc20f6b9f2e8feef3ff5498d');
Insert into doctor values (1235,1,'James Madison','Secondary Cardiologist',True,'sha256:260000$sb7KD0h59nt77VWi$a81973c98010ffa5195b70cc1eb3e55a6707c2fdeb16567165d010703548c5b1');
insert into doctor values (1236,2,'Sara Flem','Head Surgeon',True,'pbkdf2:sha256:260000$kMLGYBR90XvcT7mJ$bd4e27a4fc09b70932079f15499db03c93b870e554592a734ce5e427436851c2');
Insert into doctor values (1237,2,'Green Cox','Assistant Surgeon',True,'pbkdf2:sha256:260000$YWuPgHz32MCaqNWn$2a7ddc085e9d5ad390c8f0403ba6522ef5428b9618f1186c1cf972ce014e5f77');
insert into doctor values (1238,3,'Aaron Tony','Lead Oncologist',True,'pbkdf2:sha256:260000$INg5TFTz7ql0zYyH$957f420ab9c589d95810db70535940b9af2ce379a0b69ff198e23193c5a9dfb0');
Insert into doctor values (1239,3,'Jay Greer','Assistant Oncologist',True,'pbkdf2:sha256:260000$pzRWrB1aJLRqzi1d$1853848e0672bb4184ef96c693f397c1e384d8e2eb5b7da4c7378d5d195b51b6');
Insert into doctor values (1240,4,'Jayla Haw','Lead MedSurge Physician',True,'pbkdf2:sha256:260000$1agZ0L7YWV4B7KDn$900c8a4f727fefce5cda5c5310359e9e5519306c1dcba39b02c97ddbe414ddf6');
Insert into doctor values (1241,4,'Henry Banks','Secondary MedSurge Physician',True,'pbkdf2:sha256:260000$A8XWvpFj1CFmsVLN$173c26aedfae67102b15567b725268ff88483ab47521daba943daa7cb5baf3d4');
Insert into doctor values (1242,5,'Harry Ore','Lead Psych Physician',True,'pbkdf2:sha256:260000$0DwbwaNJnjiz3q14$c55b0a18eadda871a2bb863930a59b4389bbaf4a9ee0ec5fb05e7fe2b4558ec4');
Insert into doctor values (1243,5,'Linda Pete','Assistant Psych Physician',True,'pbkdf2:sha256:260000$vF9bmjNyM4T8zhIX$6ca98bd8d57047475a39f12f891ae975a178318d58decc389ef15c20793fcf86');
Insert into doctor values (1244,6,'MJ Jones','Lead Neurologist',True,'pbkdf2:sha256:260000$wPP3OjsfbhMqihXN$2f65b9fe2c3674079e984f6b4c884840bd39b0e32ed7dbe99d6acec614d037ff');
Insert into doctor values (1245,6,'Jimmy Dan',' Assistant Neurologist',True,'pbkdf2:sha256:260000$UkrNxTzoLfQr17iU$82b7190d187650c5322033881aa3dffe806a3ab19c293960bf0f9ff97b55cad8');
insert into doctor values (1246,7,'Harry Ban','General Physician',True,'pbkdf2:sha256:260000$BOxdOAJUEXCdle3X$5d61eeca88abeef716e9a4b06f72213cad7622608f39ba42ac356da286b8357b');
insert into doctor values (1247,7,'Phil Jane',' Assistant General Physician',True,'pbkdf2:sha256:260000$UFmHL9I1b9rO4tsX$6ff4cea44aeb0aa2f95086a4acc7f282b90b05b0a2bf5ca8a0ab433cd8ca9b7d');
Insert into doctor values (1248,8,'Sara Bans','Head Radiologist',True,'pbkdf2:sha256:260000$SzrcuKO5W27ZGFi8$c3c47a1ca0c561d3216479f0261d297c0276d7c7774eebd8005b937f9cd73b70'); 
Insert into doctor values (1249,8,'Peter Davies','Assistant Radiologist',True,'pbkdf2:sha256:260000$Qkz8vNPl48xXhaHU$ed4ef509ae8ca68c1eee450fac4d98277a70f0f83ab8259736e5142131cac1e3');


DROP TABLE IF EXISTS nurse;
CREATE TABLE nurse(
	nurse_employee_id INT,
    department_id INT,
    name VARCHAR(30),
    position VARCHAR(30),
    registered BOOLEAN,
    password VARCHAR(200),
    PRIMARY KEY(nurse_employee_id),
    FOREIGN KEY(department_id) references Department(department_id)
);

insert into nurse values (1101,1,'Joe Bean','Registered Nurse',True,'pbkdf2:sha256:260000$wQWuNKsw6WiCX7dd$aaa5661c653d5c06d8ec17129cebc1ebc79138100659fda57467d43585dab6e2');
insert into nurse values (1102,1,'Green Jimmy','Registered Nurse',True,'pbkdf2:sha256:260000$gCB0RISozNh8Geqp$51fe5137cc749f6222e2a6e51631efae4de6040a0c5bad05e453776901c8ab4a');
insert into nurse values (1103,2,'Diane Love','Registered Nurse',True,'pbkdf2:sha256:260000$9ZA9HeQzZeFQaPP4$d37feed14c5cdeebacfc41d9be7052801cdf2f06430bbdee0cf394abb555dd5d');
Insert into nurse values (1104,2,'Mario King','Registered Nurse',True,'pbkdf2:sha256:260000$dw6T5Tarj2cn4XwN$6245f1c18324c14368c7e1c35c21406861550cc8be5448cfc29c0b6e7e304a23');
insert into nurse values (1105,3,'Harry Ogfar','Registered Nurse',True,'pbkdf2:sha256:260000$eD1qS1jIPsT3GVYJ$42b2639b8b259a746f7f5d37235ca543b98a34e167d69290e9d615319bb55793');
insert into nurse values (1106,3,'Chris Coolio','Registered Nurse',True,'pbkdf2:sha256:260000$DO9LSej1RAJqa5Nr$f3b9ea5953a7602c50eb858fc31049d10b68c37725568a6791898346434962d4');
insert into nurse values (1107,4,'Lina Bland','Registered Nurse',True,'pbkdf2:sha256:260000$TELocEZQaPLYI5SP$f92c3516ba41ec96a5293e9e10e555a2c352f2c7362479b62f69df1335ac7064');
insert into nurse values (1108,4,'Olivia Straw','Registered Nurse',True,'pbkdf2:sha256:260000$boBikRdIVnYh3Ut4$23ee8c97eabe275b3e58f7a248f5c6ec786cab738c141b688443a93d8ed01566');
insert into nurse values (1109,5,'Harry Owens','Registered Nurse',True,'pbkdf2:sha256:260000$x3YEPoUx3AN9DgTe$e67268c606c3651774c48c11ee5e5f8a01ba060b08b95b24aec4fcb52f47c295');
insert into nurse values (1110,5,'Teddy Gray','Registered Nurse',True,'pbkdf2:sha256:260000$sLx6E0uAnBpNTPSA$97c254bf6cc36248b59fd54f42ba7243f055c3d0777367a33ad387da5cea2a51');
insert into nurse values (1111,6,'Tom Tiery','Registered Nurse',True,'pbkdf2:sha256:260000$5CgaEUEjyO2QWhau$db0d9ab56101747c40a03f4024cc17d47d86f749723d9dcc460e94e85b5c261c');
insert into nurse values (1112,6,'Micah Kirvy','Registered Nurse',True,'pbkdf2:sha256:260000$fZX0fEdp3qC7ipgC$c98e65955363bb4199c4c71ce623f1a8c2f27ee14d2facf1f961c89a924ea004');
insert into nurse values (1113,7,'Ari Richards','Registered Nurse',True,'pbkdf2:sha256:260000$sivYlYBdDxle0HdU$0f2ff7676f7ca800113f871812dc7a78b3d664ea2ea60a5c142b7205942e4d87');
insert into nurse values (1114,7,'Kim Jung','Registered Nurse',True,'pbkdf2:sha256:260000$YJBYwvigKaGK4isH$1db336d0e985b25069a0b9d3bad52f0621689ba8877e875f2133bf1659f8afe5');
insert into nurse values (1115,8,'Alex Cino','Registered Nurse',True,'pbkdf2:sha256:260000$OlvDnhfQchofQGCD$18833264dca8c42c96916f34203aca490dbf07deafdc4013187f1229c4d78aba');
insert into nurse values (1116,8,'Celina Binison','Registered Nurse',True,'pbkdf2:sha256:260000$LXD9aTh2iIV2xoE6$c2c270886e77a99937761a5dd2eccd5a019fbf7b817fbf1f42f01877fe4a4d29');

drop table if exists appointment;
Create table Appointment(
appointment_id INT auto_increment,
patient_id INT, 
doctor_employee_id INT, 
nurse_employee_id INT,
status VARCHAR (30),
admission_date DATETIME,
discharge_date DATETIME,
admission_type VARCHAR (40),
exam_type VARCHAR (40),
FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
FOREIGN KEY (doctor_employee_id) REFERENCES Doctor (doctor_employee_id),
FOREIGN KEY (nurse_employee_id) REFERENCES Nurse (nurse_employee_id),
Primary key (appointment_id)
);

  insert into appointment (patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type) values
  (11,1234,1101,'in progress','2022-11-29 08:00:00',null,'emergency','electrocardiogram');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type) values
 (48,1234,1101,'completed','2022-11-29 09:00:00','2022-11-30 10:00:00','emergency','echocardiogram');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (11,1234,1101,'canceled','2022-11-29 12:00:00',null,'emergency','MRI');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type) values
 (13,1235,1102,'completed','2022-11-29 08:00:00','2022-11-29 1:00:00','emergency','stress test');  
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (50,1235,1102,'canceled','2022-11-29 09:00:00',null,'emergency','electrocardiogram');
    insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (15,1236,1103,'not started','2022-11-29 08:00:00',null,'emergency','Fish hook removal');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values 
 (52,1236,1103,'completed','2022-11-29 10:00:00','2022-11-30 10:00:00','emergency','Laceration repair');
    insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (18,1237,1104,'canceled','2022-11-29 08:00:00',null,'emergency','Lumbar Puncture');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (54,1237,1104,'completed','2022-11-29 09:00:00','2022-11-30 10:00:00','emergency','Paracentesis');
    insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (10,1238,1105,'in progress','2022-11-29 11:00:00',null,'emergency','Blood test');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (56,1238,1105,'completed','2022-11-29 08:00:00','2022-11-29 10:00:00','emergency','Urine test');
    Insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (20,1239,1106,'completed','2022-11-29 15:00:00','2022-11-29 11:00:00','emergency','MRI');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (58,1239,1106,'completed','2022-11-29 08:00:00','2022-11-29 09:00:00','emergency','Biopsy');
    Insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (23,1240,1107,'in progress','2022-11-29 10:00:00',null,'emergency','Skin Therapy');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (60,1240,1107,'canceled','2022-11-29 08:00:00',null,'emergency','Gallbladder Removal');
    insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (26,1241,1108,'completed','2022-11-29 09:30:00','2022-11-29 11:30:00','emergency','ACL Repair');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (62,1241,1108,'in progress','2022-11-29 12:00:00',null,'emergency','MCL Repair');
    insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (29,1242,1109,'in progress','2022-11-29 10:00:00',null,'emergency','Psychological testing');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values 
 (63,1242,1109,'completed','2022-11-30 08:00:00','2022-11-30 10:00:00','emergency','Psychological testing');
    Insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (31,1243,1110,'completed','2022-11-29 10:00:00','2022-11-29 05:00:00','emergency','Psychological testing');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (64,1243,1110,'canceled','2022-11-30 08:00:00',null,'emergency','Psychological testing');
    Insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (36,1244,1111,'canceled','2022-11-29 10:30:00',null,'emergency','Blood test');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (66,1244,1111,'completed','2022-11-30 08:00:00','2022-11-30 10:00:00','emergency','X-Ray');
insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (38,1245,1112,'in progress','2022-11-29 12:00:00',null,'emergency','Biopsy');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (68,1245,1112,'completed','2022-11-30 08:00:00','2022-12-01 10:00:00','emergency','Blood Test');
 insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (40,1246,1113,'completed','2022-11-29 10:00:00','2022-11-29 11:30:00','emergency','Burn excision');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (70,1246,1113,'in progress','2022-11-29 12:00:00',null,'emergency','Hernia Repair');
 insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (42,1247,1114,'completed','2022-11-29 08:00:00','2022-11-30 10:00:00','emergency','Skin therapy');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (72,1247,1114,'completed','2022-11-30 11:00:00','2022-12-01 10:00:00','emergency','Urine Test');
 insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (44,1248,1115,'canceled','2022-11-29 14:00:00',null,'emergency','CT Scan');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (74,1248,1115,'canceled','2022-11-29 08:00:00',null,'emergency','Mammography');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (46,1249,1116,'completed','2022-11-29 08:00:00','2022-11-30 11:00:00','emergency','MRI');
  insert into appointment(patient_id, doctor_employee_id, nurse_employee_id, status, admission_date, discharge_date, admission_type, exam_type)values
 (76,1249,1116,'completed','2022-11-29 13:00:00','2022-11-30 03:00:00','emergency','MRI');
 
 