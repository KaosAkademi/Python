'''
# Bu bir python tekrar projesidir. Bu projede rehber isimli bir uygulamayi python dilinde tekrar ettirmeyi amacliyorum.
'''
from json import load, dumps
from os import listdir
from datetime import datetime
class Kisi:
    def __init__(self, name: str, lastname:str, tel_number: str, mail: str):
        self.name = name
        self.lastname = lastname
        self.tel_number = tel_number
        self.mail = mail
class Rehber(Kisi):
    def __init__(self, name: str, lastname:str, tel_number: str, mail: str):
        super().__init__(name, lastname, tel_number, mail)
        self.kisi ={
            'name':name,
            'lastname':lastname,
            'tel_no':tel_number,
            'mail':mail,
            }
        self.data_loc = './data/rehber.json'

    def status():
        '''
        Son guncelleme tarihini getirir.

        Returns:
            str: Son guncelleme tarihi
        '''
        data_loc = './data/rehber.json'
        with open(data_loc, 'r') as f:
            d = load(f)
        last_update = d['degistirme_tarihi']
        return last_update
    def re_identification(self) -> bool:
        '''
        Telefon numarasına göre kayıtlı bir kişi var mı kontrol eder

        Returns:
            bool: Telefon numarasına göre kayıtlı bir kişi varsa True, yoksa False
        '''

        ...
    @staticmethod
    def check_valid_number(tel_no) -> bool:
        # Türkiye'nin uluslararası telefon kodu
        '''
        Telefon numarasının geçerli olup olmadığını kontrol eder.

        Parameters:
            tel_no (str): Telefon numarası

        Returns:
            bool: Telefon numarası geçerli ise True, yoksa False
        '''
        turkiye_kodu = "+90"
        # Telefon numarasının "+90" ile başlaması ve 13 karakter uzunluğunda olması gerekir
        return (tel_no.startswith(turkiye_kodu) and len(tel_no) == 13)

    def check_valid_mail(mail: str) -> bool:
        # [blablabla, @(bolundu), mail.com ]
        '''
        Mail adresinin geçerli olup olmadığını kontrol eder.

        Parameters:
            mail (str): Mail adresi

        Returns:
            bool: Mail adresi geçerli ise True, yoksa False
        '''
        parts = mail.split('@')
        return len(parts) == 2 and '.' in parts[1]

    def check_is_exist(self) -> bool:
        '''
        Kayıtlı bir kişi olup olmadığını kontrol eder.

        Returns:
            bool: Kayıtlı ise True, yoksa False
        '''
        with open(self.data_loc, "r") as fileObject:
            data = load(fileObject)
            rehber = data['rehber']
            for kisi in rehber:
                if kisi['tel_no'] == self.kisi['tel_no']:
                    return True # Kayitli
            return False # Kayitli degil
    def save(self):
        '''
        Kişinin bilgilerini kaydeder.

        Returns:
            None
        '''
        if self.check_is_exist():
            print("Zaten kayıtlı")
        if "rehber.json" in listdir('./data'):
            with open(self.data_loc, 'r') as f:
                data = load(f)
                data.get("rehber").append(self.kisi)
                data['degistirme_tarihi'] = str(datetime.now())[10]
                data = dumps(data, indent=4)
                try:
                    with open(self.data_loc, 'w') as f:
                        f.write(data)
                        print("Kayıt yapıldı")
                except:
                    print('bir hata ile karşılaşıldı')

        else:
            with open(self.data_loc, 'r') as f:
                data = load(f)
                data.get("rehber").append(self.kisi)
                print("Kayıt yapıldı")
    @staticmethod
    def get_persons():
        data_loc = './data/rehber.json'
        with open(data_loc, 'r') as f:
            data = load(f)
        return data['rehber']
    @staticmethod
    def delete(tel_no: str):
        '''
        Kayıtlı bir kişiyi siler.

        Parameters:
            tel_no (str): Telefon numarası

        Returns:
            None
        '''
        data_loc = './data/rehber.json'
        if "rehber.json" in listdir('./data'):
            with open(data_loc, 'r') as f:
                data = load(f)['rehber']
                new_data = []
            for i in data:
                if i['tel_no'] == tel_no:
                    pass
                else:
                    new_data.append(i)
            with open(data_loc, 'r') as f:
                data = load(f)
                data['rehber'] = new_data
                data['degistirme_tarihi'] = str(datetime.now())[10]
                data = dumps(data, indent=4)
                try:
                    with open(data_loc, 'w') as f:
                        f.write(data)
                        print("Kayıt silindi")
                except:
                    print('bir hata ile karşılaşıldı')
    @staticmethod
    def update_person(ex_number: str, name:str, lastname:str, mail:str, tel_no: str):
        data_loc = './data/rehber.json'
        if "rehber.json" in listdir('./data'):
            with open(data_loc, 'r') as f:
                data = load(f)
                new_data = []
                for i in data['rehber']:
                    if i['tel_no'] == ex_number:
                        i['tel_no'] = tel_no
                        i['name'] = name
                        i['lastname'] = lastname
                        i['mail'] = mail
                        data['degistirme_tarihi'] = str(datetime.now())[10]
                        new_data.append(i)
                    else:
                        new_data.append(i)
                data['rehber'] = new_data
                data = dumps(data, indent=4)

            try:
                with open(data_loc, 'w') as f:
                    f.write(data)
                    print("Kayıt değiştirildi")
            except:
                print('bir hata ile karşılaşıldı')
    @staticmethod
    def find_person(tel_no: str) ->bool:
        data_loc = './data/rehber.json'
        with open(data_loc, 'r') as f:
            data = load(f)
        for i in data['rehber']:
            if i['tel_no'] == tel_no:
                return True

        else: return False


def main():
    """
    Rehber uygulamasının ana fonksiyonu. Kullanıcıdan işlem seçimi alır ve ilgili
    işlemi gerçekleştirir. Kullanıcıya rehberdeki kişileri gösterme, yeni kişi kaydetme,
    numara silme veya kişiyi güncelleme seçenekleri sunar.

    Kullanıcı Seçenekleri:
        1 - Telefon numaralarını görüntüle
        2 - Yeni telefon numarası kaydet
        3 - Telefon numarasını sil
        4 - Kişiyi güncelle
        5 - Çıkış yap

    Sürekli olarak kullanıcıdan bir seçim yapmasını ister ve yapılan seçime göre
    uygun fonksiyonu çağırır. Seçim listesi dışında bir giriş yapılırsa kullanıcıyı
    uyarır.
    """

    def chosen(argument) -> None:
        def show_numbers():
            person = Rehber.get_persons()
            for kisi in person:
                print(f"""
                Name: {kisi['name']}
                Lastname: {kisi['lastname']}
                mail: {kisi['mail']}
                tel no: {kisi['tel_no']}
                """)
        def save_numbers():
                while True:
                    tel_no = input("Telefon numarasını bu formatta giriniz (+905555555555): ")
                    if Rehber.check_valid_number(tel_no=tel_no):
                        break
                    else:
                        print("Lutfen gecerli bir tel giriniz!")

                name = input("Isim giriniz: ")
                lastname = input("Soy isimini giriniz: ")
                while True:
                    mail = input("Mail giriniz: ")
                    if Rehber.check_valid_mail(mail=mail):
                        break
                    else:
                        print("Lutfen gecerli bir mail giriniz!")

                P = Rehber(name=name, lastname=lastname, tel_number=tel_no, mail=mail)
                P.save()
        def del_number() -> None:
            while True:
                tel_no = input("Telefon numarasını bu formatta giriniz (+905555555555): ")
                if Rehber.check_valid_number(tel_no=tel_no):
                    break
                else:
                    print("Lutfen gecerli bir tel giriniz!")
            Rehber.delete(tel_no=tel_no)
        def update_person():
            while True:
                ex_number = input("Telefon numarasını bu formatta giriniz (+905555555555): ")
                if Rehber.check_valid_number(tel_no=ex_number):
                    break
                else:
                    print("Lutfen gecerli bir tel giriniz!")
            if Rehber.find_person(tel_no=ex_number):
                while True:
                    tel_no = input("Lutfen yeni Telefon numarasını bu formatta giriniz (+905555555555): ")
                    if Rehber.check_valid_number(tel_no=tel_no):
                        break
                    else:
                        print("Lutfen kayıtlı bir tel giriniz!")

                name = input("Isim giriniz: ")
                lastname = input("Soy isimini giriniz: ")
                while True:
                    mail = input("Mail giriniz: ")
                    if Rehber.check_valid_mail(mail=mail):
                        break
                    else:
                        print("Lutfen gecerli bir mail giriniz!")

                Rehber.update_person(ex_number=ex_number,tel_no=tel_no,name=name, lastname=lastname, mail=mail)


        if argument not in '12345':
            print('Lutfen seciniz!')
        else:
            switch_case = {
                    '1': show_numbers,
                    '2': save_numbers,
                    '3': del_number,
                    '4': update_person,
                    '5': exit
                }

            return switch_case.get(argument)()

    while True:
        last_update = Rehber.status()
        print(f"""
                ############## REHBER #################
                    son degisme :{last_update[:10]}
                #   1 - Telefon numaraları            #
                #   2 - Telefon Kayit Et              #
                #   3 - Telefon numarasi sil          #
                #   4 - Kisi Guncelle                 #
                #   5 - Cikis Yap                     #
                #                                     #
                #######################################
                """)
        selected = input('Hoşgeldiniz Ne yapmak istiyorsunuz: ')
        chosen(selected)

if __name__ == '__main__':
    main()
