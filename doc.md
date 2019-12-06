

## Import Formats

It is necessary that the files have a defined format to ensure that the import works properly.

### Participant import 
This is the file to import participants / athletes from a file.

The format of the file must be a MS Excel sheet. The order of the columns does not matter, but it is important that the column Names are in the first row and have the excact same spelling as in the tables below.
All of the following names must be written in the Header.

The excel file must also contain 2 Sheets. The sheet "Meldungsliste" contains the following columns and is needed to know which athletes are in the competitions.

#### Sheet "Meldungsliste"

| Column Name | Description | Mandatory |
| ---------- | ------------ | ------------- |
| Name      | Last name of the athlete |  Yes |
| Vorname   | First name of the athlete | Yes |
| Jahrgang  | Birthyear of the athlete | Yes |
| Geschlecht | The sex of the athlete | Yes |
| Verein | The club of the athlete | No|

#### Sheet "Klassen"
| Column Name | Description | Mandatory |
| ---------- | ------------ | ------------- |
| Klasse      | The name of the class group |  Yes |
| Geschlecht  | The sex of athletes that should start in this class. | Yes|
|jüngstJahrg | The birthYear of the youngest athletes. (e.g. 2013) | Yes|
|ältestJahrg | The birthYear of the oldest athletes  (e.g. 1939) | 




## Special Names in SQL Tables
The here listed tables should have constant names

### Athlete

tablename : "athletes"

|Name of Table Attribute    | Description|  
| :--------------------    | :--------|  
| name                      | Last name of the athlete (e.g. Arruba)|
| firstName                 | First name of the athlete (e.g. Richie) |
| classGroup                | The name of the group in that the athlete starts (e.g. Schüler 12 Männlich)
| birthYear                 | The Year the athelete was born in. (e.g. 1996)
| sex                       | Sex of the athelete. (e.g. 'female')
| club                      | Club of the Athlete (e.g. "WSV Reit im Winkl)






## Known Issues

- Logging is not implemented
- Error Handling is not implemented