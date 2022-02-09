from django.db import models
from datetime import datetime
# from osgeo import gdal


# lists of options
# cities_name_list=(("Abbotabad","Abbotabad"),("Bahawalpur","Bahawalpur"),("Charsaddah","Charsaddah"),("Dera Ghazi Khan","Dera Ghazi Khan"),("Faisalabad","Faisalabad"),("Gawadar","Gawadar"),("Islamabad","Islamabad"),("Rawalpindi","Rawalpindi"),("Karachi","Karachi"),("Lahore","Lahore"),("Multan","Multan"),("None","None"))

district_list = (("Gawadar","Gawadar"),("Jaffarabad","Jaffarabad"),("Pishin","Pishin"),("Quetta","Quetta"))

teshil_list = (("Gawadar","Gawadar"),("Jiwani","Jiwani"),("Ormara","Ormara"),("Pasni","Pasni"))

patwarcircle_list = (("Ankara","Ankara"),("Chatti","Chatti"),("Chib Kalamati","Chib Kalamati"),("City","City"),("Dhor Ghatti", "Dhor Ghatti"),("Gurandani","Gurandani"),("Jorkaan","Jorkaan"),("Karwaat","Karwaat"),("Ormara","Ormara"),("Paleri","Paleri"),("Pishukaan","Pishukaan"),("Settlement","Settlement"),("Shaabi","Shaabi"),("Surbandar","Surbandar"))

mauza_list = (("Ankara Junoobi","Ankara Junoobi"),("Ankara Shumali","Ankara Shumali"),("Chatti Junoobi","Chatti Junoobi"),("Chatti Shumali","Chatti Shumali"),("Darbela Shumali","Darbela Shumali"),("Kappar Gharbi","Kappar Gharbi"),("Kappar Sharqi","Kappar Sharqi"),("Mouza Baan","Mouza Baan"),("Mouza Ballada","Mouza Ballada"),("Mouza Bandari","Mouza Bandari"),("Mouza Bandi","Mouza Bandi"),("Mouza Basool","Mouza Basool"),("Mouza Chakkuli","Mouza Chakkuli"),("Mouza Chandi","Mouza Chandi"),("Mouza Cheb Rakhani","Mouza Cheb Rakhani"),("Mouza Chib Kalmati","Mouza Chib Kalmati"),("Mouza Chukken","Mouza Chukken"),("Mouza Chullani","Mouza Chullani"),("Mouza Churbandar","Mouza Churbandar"),("Mouza Daat","Mouza Daat"),("Mouza Darbela Junoobi","Mouza Darbela Junoobi"),("Mouza Door Ghatti","Mouza Door Ghatti"),("Mouza Dosi","Mouza Dosi"),("Mouza Espiyak","Mouza Espiyak"),("Mouza Faqeerabad","Mouza Faqeerabad"),("Mouza Ganz","Mouza Ganz"),("Mouza Garook","Mouza Garook"),("Mouza Garruki","Mouza Garruki"),("Mouza Gazdaan Bal","Mouza Gazdaan Bal"),("Mouza Ghamarwo","Mouza Ghamarwo"),("Mouza Ghatti","Mouza Ghatti"),("Mouza Ghoorhad","Mouza Ghoorhad"),("Mouza Gurandani Junoobi","Mouza Gurandani Junoobi"),("Mouza Gurrani","Mouza Gurrani"),("Mouza Haegani","Mouza Haegani"),("Mouza Jaffary","Mouza Jaffary"),("Mouza Jahoorkan","Mouza Jahoorkan"),("Mouza Kahoordan","Mouza Kahoordan"),("Mouza Kalmat","Mouza Kalmat"),("Mouza Kandalik","Mouza Kandalik"),("Mouza Kandasol","Mouza Kandasol"),("Mouza Kargoshki","Mouza Kargoshki"),("Mouza Keya Kalaat","Mouza Keya Kalaat"),("Mouza Kunnar Bal","Mouza Kunnar Bal"),("Mouza Maazwar","Mouza Maazwar"),("Mouza Makola Garbi","Mouza Makola Garbi"),("Mouza Makola Sharqi","Mouza Makola Sharqi"),("Mouza Maro","Mouza Maro"),("Mouza Mazzhani","Mouza Mazzhani"),("Mouza Mhal","Mouza Mhal"),("Mouza Nalient Sher Muhammad Bazar","Mouza Nalient Sher Muhammad Bazar"),("Mouza Nigore Shareef","Mouza Nigore Shareef"),("Mouza Okar","Mouza Okar"),("Mouza Ormara","Mouza Ormara"),("Mouza Paleri Gharbi","Mouza Paleri Gharbi"),("Mouza Paleri Sharqi","Mouza Paleri Sharqi"),("Mouza Panwan","Mouza Panwan"),("Mouza Passo","Mouza Passo"),("Mouza Pishal","Mouza Pishal"),("Mouza Pishukaan","Mouza Pishukaan"),("Mouza Praheen Tohk","Mouza Praheen Tohk"),("Mouza Qalandari","Mouza Qalandari"),("Mouza Rach","Mouza Rach"),("Mouza Robar","Mouza Robar"),("Mouza Rombdo","Mouza Rombdo"),("Mouza Sahiji Faqeer Muhammad Bazar","Mouza Sahiji Faqeer Muhammad Bazar"),("Mouza Sahiji Hassan Bazar","Mouza Sahiji Hassan Bazar"),("Mouza Sarchash","Mouza Sarchash"),("Mouza Shaabi","Mouza Shaabi"),("Mouza Shadi Kaur","Mouza Shadi Kaur"),("Mouza Shadikaur Junoobi","Mouza Shadikaur Junoobi"),("Mouza Sham","Mouza Sham"),("Mouza Shanekani Dar","Mouza Shanekani Dar"),("Mouza Shatangi","Mouza Shatangi"),("Mouza Shumal Bandan","Mouza Shumal Bandan"),("Mouza Sukhni","Mouza Sukhni"),("Mouza Surbandar","Mouza Surbandar"),("Mouza Tank","Mouza Tank"),("Mouza Thsk","Mouza Thsk"),("Mouza Washeen Dor","Mouza Washeen Dor"),("Mouza Zareen","Mouza Zareen"),("Mouza Ziarat Machi Gharbi","Mouza Ziarat Machi Gharbi"),("Mouza Ziarat Machi Sharqi","Mouza Ziarat Machi Sharqi"),("Ward Assa","Ward Assa"),("Ward Bagh Bazar Junoobi","Ward Bagh Bazar Junoobi"),("Ward Bagh Bazar Shumali","Ward Bagh Bazar Shumali"),("Ward Baloch","Ward Baloch"),("Ward Bangla Bazar","Ward Bangla Bazar"),("Ward Captain Murad Baksh","Ward Captain Murad Baksh"),("Ward Gazrawan","Ward Gazrawan"),("Ward Ghulam Sarwar Muhalla Junoobi","Ward Ghulam Sarwar Muhalla Junoobi"),("Ward Habib Lashkari","Ward Habib Lashkari"),("Ward Ismailia","Ward Ismailia"),("Ward Kareem Baksh","Ward Kareem Baksh"),("Ward Khauda Amanullah","Ward Khauda Amanullah"),("Ward Kohbun","Ward Kohbun"),("Ward Kohsar Garbi","Ward Kohsar Garbi"),("Ward Kohsar Sharqi","Ward Kohsar Sharqi"),("Ward Kolgari","Ward Kolgari"),("Ward Kummadi","Ward Kummadi"),("Ward Mahigeeran Garbi","Ward Mahigeeran Garbi"),("Ward Mir Lal Baksh","Ward Mir Lal Baksh"),("Ward Mir Rehmat Garbi","Ward Mir Rehmat Garbi"),("Ward Mujahid","Ward Mujahid"),("Ward Mullah Band","Ward Mullah Band"),("Ward Mullah Hashim","Ward Mullah Hashim"),("Ward Naguman","Ward Naguman"),("Ward Navy","Ward Navy"),("Ward Negwari","Ward Negwari"),("Ward Ormari Junobi","Ward Ormari Junobi"),("Ward Ormari Shumali","Ward Ormari Shumali"),("Ward Prahag Muhallah","Ward Prahag Muhallah"),("Ward Purana Market","Ward Purana Market"),("Ward Qazi Rehmat Sharqi","Ward Qazi Rehmat Sharqi"),("Ward Raeesani","Ward Raeesani"),("Ward Saleh Muhammad","Ward Saleh Muhammad"),("Ward Senator Ishaq","Ward Senator Ishaq"),("Ward Shadoband","Ward Shadoband"),("Ward Shambay Ismail","Ward Shambay Ismail"),("Ward Shehzada Bazar Janoobi","Ward Shehzada Bazar Janoobi"),("Ward Sheikh Umer","Ward Sheikh Umer"),("Ward Sohrabi","Ward Sohrabi"),("Ward Thana","Ward Thana"),("Ward Tobag","Ward Tobag"),("Ward Usmania","Ward Usmania"),("Ward Zahoor Shah Hashmi","Ward Zahoor Shah Hashmi"),("Ward Zobag Muhalla Junoobi","Ward Zobag Muhalla Junoobi"))

massavi_sheets =(("A-1","A-1"),
("A-2","A-2"),
("A-3","A-3"),
("A-4","A-4"),
("A-5","A-5"),
("A-6","A-6"),
("A-7","A-7"),
("A-8","A-8"),
("A-9","A-9"),
("A-10","A-10"),
("A-11","A-11"),
("A-12","A-12"),
("A-13","A-13"),
("A-14","A-14"),
("A-15","A-15"),
("A-16","A-16"),
("B-1","B-1"),
("B-2","B-2"),
("B-3","B-3"),
("B-4","B-4"),
("B-5","B-5"),
("B-6","B-6"),
("B-7","B-7"),
("B-8","B-8"),
("B-9","B-9"),
("B-10","B-10"),
("B-11","B-11"),
("B-12","B-12"),
("B-13","B-13"),
("B-14","B-14"),
("B-15","B-15"),
("B-16","B-16"),
("J-1","J-1"),
("J-2","J-2"),
("J-3","J-3"),
("J-4","J-4"),
("J-5","J-5"),
("J-6","J-6"),
("J-7","J-7"),
("J-8","J-8"),
("J-9","J-9"),
("J-10","J-10"),
("J-11","J-11"),
("J-12","J-12"),
("J-13","J-13"),
("J-14","J-14"),
("J-15","J-15"),
("J-16","J-16"),
("D-1","D-1"),
("D-2","D-2"),
("D-3","D-3"),
("D-4","D-4"),
("D-5","D-5"),
("D-6","D-6"),
("D-7","D-7"),
("D-8","D-8"),
("D-9","D-9"),
("D-10","D-10"),
("D-11","D-11"),
("D-12","D-12"),
("D-13","D-13"),
("D-14","D-14"),
("D-15","D-15"),
("D-16","D-16"),
("H-1","H-1"),
("H-2","H-2"),
("H-3","H-3"),
("H-4","H-4"),
("H-5","H-5"),
("H-6","H-6"),
("H-7","H-7"),
("H-8","H-8"),
("H-9","H-9"),
("H-10","H-10"),
("H-11","H-11"),
("H-12","H-12"),
("H-13","H-13"),
("H-14","H-14"),
("H-15","H-15"),
("H-16","H-16"),
("W-1","W-1"),
("W-2","W-2"),
("W-3","W-3"),
("W-4","W-4"),
("W-5","W-5"),
("W-6","W-6"),
("W-7","W-7"),
("W-8","W-8"),
("W-9","W-9"),
("W-10","W-10"),
("W-11","W-11"),
("W-12","W-12"),
("W-13","W-13"),
("W-14","W-14"),
("W-15","W-15"),
("W-16","W-16"),
("Z-1","Z-1"),
("Z-2","Z-2"),
("Z-3","Z-3"),
("Z-4","Z-4"),
("Z-5","Z-5"),
("Z-6","Z-6"),
("Z-7","Z-7"),
("Z-8","Z-8"),
("Z-9","Z-9"),
("Z-10","Z-10"),
("Z-11","Z-11"),
("Z-12","Z-12"),
("Z-13","Z-13"),
("Z-14","Z-14"),
("Z-15","Z-15"),
("Z-16","Z-16"),
("T-1","T-1"),
("T-2","T-2"),
("T-3","T-3"),
("T-4","T-4"),
("T-5","T-5"),
("T-6","T-6"),
("T-7","T-7"),
("T-8","T-8"),
("T-9","T-9"),
("T-10","T-10"),
("T-11","T-11"),
("T-12","T-12"),
("T-13","T-13"),
("T-14","T-14"),
("T-15","T-15"),
("T-16","T-16"),
("Y-1","Y-1"),
("Y-2","Y-2"),
("Y-3","Y-3"),
("Y-4","Y-4"),
("Y-5","Y-5"),
("Y-6","Y-6"),
("Y-7","Y-7"),
("Y-8","Y-8"),
("Y-9","Y-9"),
("Y-10","Y-10"),
("Y-11","Y-11"),
("Y-12","Y-12"),
("Y-13","Y-13"),
("Y-14","Y-14"),
("Y-15","Y-15"),
("Y-16","Y-16"),
("K-1","K-1"),
("K-2","K-2"),
("K-3","K-3"),
("K-4","K-4"),
("K-5","K-5"),
("K-6","K-6"),
("K-7","K-7"),
("K-8","K-8"),
("K-9","K-9"),
("K-10","K-10"),
("K-11","K-11"),
("K-12","K-12"),
("K-13","K-13"),
("K-14","K-14"),
("K-15","K-15"),
("K-16","K-16"),
("L-1","L-1"),
("L-2","L-2"),
("L-3","L-3"),
("L-4","L-4"),
("L-5","L-5"),
("L-6","L-6"),
("L-7","L-7"),
("L-8","L-8"),
("L-9","L-9"),
("L-10","L-10"),
("L-11","L-11"),
("L-12","L-12"),
("L-13","L-13"),
("L-14","L-14"),
("L-15","L-15"),
("L-16","L-16"),
("M-1","M-1"),
("M-2","M-2"),
("M-3","M-3"),
("M-4","M-4"),
("M-5","M-5"),
("M-6","M-6"),
("M-7","M-7"),
("M-8","M-8"),
("M-9","M-9"),
("M-10","M-10"),
("M-11","M-11"),
("M-12","M-12"),
("M-13","M-13"),
("M-14","M-14"),
("M-15","M-15"),
("M-16","M-16"),
("N-1","N-1"),
("N-2","N-2"),
("N-3","N-3"),
("N-4","N-4"),
("N-5","N-5"),
("N-6","N-6"),
("N-7","N-7"),
("N-8","N-8"),
("N-9","N-9"),
("N-10","N-10"),
("N-11","N-11"),
("N-12","N-12"),
("N-13","N-13"),
("N-14","N-14"),
("N-15","N-15"),
("N-16","N-16"),
("S-1","S-1"),
("S-2","S-2"),
("S-3","S-3"),
("S-4","S-4"),
("S-5","S-5"),
("S-6","S-6"),
("S-7","S-7"),
("S-8","S-8"),
("S-9","S-9"),
("S-10","S-10"),
("S-11","S-11"),
("S-12","S-12"),
("S-13","S-13"),
("S-14","S-14"),
("S-15","S-15"),
("S-16","S-16"),
("E-1","E-1"),
("E-2","E-2"),
("E-3","E-3"),
("E-4","E-4"),
("E-5","E-5"),
("E-6","E-6"),
("E-7","E-7"),
("E-8","E-8"),
("E-9","E-9"),
("E-10","E-10"),
("E-11","E-11"),
("E-12","E-12"),
("E-13","E-13"),
("E-14","E-14"),
("E-15","E-15"),
("E-16","E-16"),
("F-1","F-1"),
("F-2","F-2"),
("F-3","F-3"),
("F-4","F-4"),
("F-5","F-5"),
("F-6","F-6"),
("F-7","F-7"),
("F-8","F-8"),
("F-9","F-9"),
("F-10","F-10"),
("F-11","F-11"),
("F-12","F-12"),
("F-13","F-13"),
("F-14","F-14"),
("F-15","F-15"),
("F-16","F-16"),
("SW-1","SW-1"),
("SW-2","SW-2"),
("SW-3","SW-3"),
("SW-4","SW-4"),
("SW-5","SW-5"),
("SW-6","SW-6"),
("SW-7","SW-7"),
("SW-8","SW-8"),
("SW-9","SW-9"),
("SW-10","SW-10"),
("SW-11","SW-11"),
("SW-12","SW-12"),
("SW-13","SW-13"),
("SW-14","SW-14"),
("SW-15","SW-15"),
("SW-16","SW-16"),
("Q-1","Q-1"),
("Q-2","Q-2"),
("Q-3","Q-3"),
("Q-4","Q-4"),
("Q-5","Q-5"),
("Q-6","Q-6"),
("Q-7","Q-7"),
("Q-8","Q-8"),
("Q-9","Q-9"),
("Q-10","Q-10"),
("Q-11","Q-11"),
("Q-12","Q-12"),
("Q-13","Q-13"),
("Q-14","Q-14"),
("Q-15","Q-15"),
("Q-16","Q-16"),
("R-1","R-1"),
("R-2","R-2"),
("R-3","R-3"),
("R-4","R-4"),
("R-5","R-5"),
("R-6","R-6"),
("R-7","R-7"),
("R-8","R-8"),
("R-9","R-9"),
("R-10","R-10"),
("R-11","R-11"),
("R-12","R-12"),
("R-13","R-13"),
("R-14","R-14"),
("R-15","R-15"),
("R-16","R-16"),
("HI-1","HI-1"),
("HI-2","HI-2"),
("HI-3","HI-3"),
("HI-4","HI-4"),
("HI-5","HI-5"),
("HI-6","HI-6"),
("HI-7","HI-7"),
("HI-8","HI-8"),
("HI-9","HI-9"),
("HI-10","HI-10"),
("HI-11","HI-11"),
("HI-12","HI-12"),
("HI-13","HI-13"),
("HI-14","HI-14"),
("HI-15","HI-15"),
("HI-16","HI-16"),
("SH-1","SH-1"),
("SH-2","SH-2"),
("SH-3","SH-3"),
("SH-4","SH-4"),
("SH-5","SH-5"),
("SH-6","SH-6"),
("SH-7","SH-7"),
("SH-8","SH-8"),
("SH-9","SH-9"),
("SH-10","SH-10"),
("SH-11","SH-11"),
("SH-12","SH-12"),
("SH-13","SH-13"),
("SH-14","SH-14"),
("SH-15","SH-15"),
("SH-16","SH-16"),
("TH-1","TH-1"),
("TH-2","TH-2"),
("TH-3","TH-3"),
("TH-4","TH-4"),
("TH-5","TH-5"),
("TH-6","TH-6"),
("TH-7","TH-7"),
("TH-8","TH-8"),
("TH-9","TH-9"),
("TH-10","TH-10"),
("TH-11","TH-11"),
("TH-12","TH-12"),
("TH-13","TH-13"),
("TH-14","TH-14"),
("TH-15","TH-15"),
("TH-16","TH-16"),
("C-1","C-1"),
("C-2","C-2"),
("C-3","C-3"),
("C-4","C-4"),
("C-5","C-5"),
("C-6","C-6"),
("C-7","C-7"),
("C-8","C-8"),
("C-9","C-9"),
("C-10","C-10"),
("C-11","C-11"),
("C-12","C-12"),
("C-13","C-13"),
("C-14","C-14"),
("C-15","C-15"),
("C-16","C-16"))





# define upload path function
def content_file_name(instance, filename):
    name, ext = filename.split(')')
    file_path = 'images/{mauza}/{form_id}{ext}'.format(
          form_id=instance.form_id, mauza=instance.mauza, ext=ext) 
    return file_path


# Create your models here.
class UploadImage(models.Model):  
    
    form_id = models.CharField(max_length=100, primary_key=True, unique=True, default=1) 
    
    time_now = models.DateField(default=datetime.now,blank=True)
    
    image = models.ImageField(max_length=200,upload_to= content_file_name, null=True, blank=True)
    
    type_data = models.CharField(max_length=50, null=True, blank=True, default="Massavi")
    
    district = models.CharField(max_length=50, null=True, blank=True, choices = district_list)
    
    tehsil = models.CharField(max_length=50, null=True, blank=True, choices = teshil_list)
    
    patwar_circle = models.CharField(max_length=50, null=True, blank=True, choices = patwarcircle_list)
    
    mauza = models.CharField(max_length=50, null=True, blank=True, choices = mauza_list)
    
    massavi_no = models.CharField(max_length=50, null=True, blank=True,choices = massavi_sheets)


    
    
    
    
    def __str__(self):  
        return self.form_id 
  
  
    def save(self, *args, **kwargs):
        
        self.form_id = f'{self.district}_{self.tehsil}_{self.patwar_circle}_{self.mauza}_{self.massavi_no}'
        super(UploadImage,self).save(*args, **kwargs)
         
        
        # if IntegrityError:
        #         return HttpResponse("ERROR: form already exists!")
        
        
        
        # student=UploadImage.objects.get(pk=form_id)
        # student.save()
        # print (student.form_id)
    
    
    
    # def get_formid_value():
    
    #     formid_value = UploadImage.objects.get(pk=form_id)
    #     print(formid_value)
    #     return formid_value
    
    # my_object = get_formid_value()
    
    

    
    
