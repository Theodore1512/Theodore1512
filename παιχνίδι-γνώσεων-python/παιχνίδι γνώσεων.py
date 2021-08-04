﻿#
# Σχ. Έτος 2020-21
# Θεόδωρος Ελευθέριος Βασιλικός
# Νίκος Καλλίτσης
# Παιχνίδι γνώσεων για απόφοιτους του Γυμνασίου ©
#

#Variable για τις λάθος απαντήσεις:
pl = 0

# όλα τα functions για τις ερωτήσεις:
def Πληροφορική_προσπάθειες():
    category1 = input('Πληροφορική ')
    if category1 == "Ναι" or category1 == "ναι" or category1 == 'ΝΑΙ':
        print('\n')
        print("Ερώτηση 1:")
        print('-'*10)
        πληρ1προ = 2
        while πληρ1προ > 0:
            print("CPU, GPU, SSD, HDD ή USB;")
            qu1 = input("Πως λέγεται σε συντομογραφία η κάρτα γραφικών;")
            if qu1 == 'GPU'or qu1 == 'gpu'or qu1 == 'G.P.U.' or qu1 == 'Gpu':
                print('Μπράβο το G.P.U. είναι το Graphics processing unit, δηλαδή εκεί που επεξεργάζονται τα γραφικά, αυτό που βλέπεις στην οθόνη!')
                πληρ1προ -= 5
            else:
                print('Μια μικρή βοήθεια: όπου βλέπεις D στο τέλος μιας λέξης από τις παραπάνω είναι Disk (δίσκος)...')
                πληρ1προ -= 1
                print(f'Σου απομένουν {πληρ1προ} προσπάθειες')
                if πληρ1προ <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 2:")
        print('-'*10)
        πληρ2προ = 2
        while πληρ2προ > 0:
            print("Word, Notepad, Pages, OpenOffice, Libre Writer")
            qu2 = input("Ποιά από τις παραπάνω είναι εφαρμογή της Microsoft;")
            if qu2 == 'Word' or qu2 == 'word'or qu2 == 'WORD':
                print('Καλός καλός! Έτσι πληροφοριακά όλα τα παραπάνω προγράμματα είναι για επεξεργασία κειμένου, αλλά μόνο το Word είναι της Microsoft.')
                πληρ2προ -= 5
            else:
                print('Δε νομίζω πως είναι δύσκολο... μια μικρή βοήθεια το Pages δεν είναι πρόγραμμα των windows, είναι εφαρμογή της Apple.')
                πληρ2προ -= 1
                print(f'Σου απομένουν {πληρ2προ} προσπάθειες')
                if πληρ2προ <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    pl += 1
                    break
        print('-'*5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 3:")
        print('-'*10)
        πληρ3προ = 3
        while πληρ3προ > 0:
            print("Intel, AMD, Apple, NVidia")
            qu3 = input("Ποιά από τις παραπάνω ΔΕΝ είναι μάρκα επεξεργαστών;")
            if qu3 == "NVidia" or qu3 == "nvidia" or qu3 == "NVIDIA":
                print("Πολύ σωστά, η NVidia είναι η πιο γνωστή εταιρεία που παράγει κάρτες γραφικών(GPU).")
                πληρ3προ -= 5
            else:
                print('Λίγο ανεβάσαμε τον πήχη; Δεν μιλάω συγκεκριμένα για επεξεργαστές υπολογιστών... και τα κινητά τηλέφωνα (π.χ.) έχουν επεξεργαστή!')
                πληρ3προ -= 1
                print(f'Σου απομένουν {πληρ3προ} προσπάθειες')
                if πληρ3προ <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
    else:
        print('Πάμε παρακάτω...')
def Γλώσσα_Λογοτεχνία_προσπάθειες():
    category2 = input('Γλώσσα - Λογοτεχνία ')
    if category2 == "Ναι"or category2 == "ναι" or category2 == "ΝΑΙ":
        print('\n')
        print("Ερώτηση 1:")
        print('-'*10)        
        λογ1 = 2
        while λογ1 > 0:
            print("Φεραίος, Κορνάρος, Ελύτης")
            que1 = input("Ποιός έγραψε τον Θούριο;")
            if que1 == "Φεραίος" or que1 == "Φερέος" or que1 == "φεραίος" or que1 == "ΦΕΡΑΙΟΣ":
                print("Δεν έχω λόγια!!!")
                λογ1 -= 5
            else:
                print('Προσπάθησε ξανά... απλά να ξέρεις ο Οδ. Ελύτης ήταν ένας από τους πιο σπουδαίους ποιητές της Ελλάδας!')
                λογ1 -= 1
                print(f'Σου απομένουν {λογ1} προσπάθειες')
                if λογ1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 2")
        print('-'*10)
        λογ2 = 2
        while λογ2 > 0:
            print("Αντίθεση, Eιρωνεία, Έλλειψη")
            que2 = input("Ποιό σχήμα λόγου παρατηρείτε στο παράδειγμα: Ωραία τα κατάφερες!")
            if que2 == 'Ειρωνεία' or que2 == 'ειρωνεία' or que2 == 'ΕΙΡΩΝΕΙΑ' or que2 == 'Ειρονεία':
                print('Πολύ καλός παίχτης! Αν το βρήκες με τη πρώτη Μπράβο, αλλιώς δε πειράζει έμαθες...')
                λογ2 -= 5
            else:
                print('Μήπως εσύ έχεις έλλειψη; Για δες ξανά φίλε μου! (ΑΝΤΙΘΕΣΗ)')
                λογ2 -= 1
                print(f'Σου απομένουν {λογ2} προσπάθειες')
                if λογ2 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 3")
        print('-'*10)
        λογ3 = 2
        while λογ3 > 0:
            print("Παραγράφους, Ομοιοκαταληξίες ή Στροφές")
            ques1 = input("Το ποίημα έχει πάντα...")
            if ques1 == 'Στροφές'or ques1 == 'στροφές' or ques1 == 'Στροφες':
                print('Το βρήκες! Ομοιοκαταληξίες δεν έχουν όλα τα ποιήματα, ειδικότερα αν ανήκουν στη μοντέρνα ποίηση! Στροφές όμως έχουν όλα!')
                λογ3 -= 5
            else:
                print('Σε ρώτησα συγκεκριμένα τι έχει ένα ποίημα ΠΑΝΤΑ... εκ φύσεως πώς το λένε; Ξανά!')
                λογ3 -= 1
                print(f'Σου απομένουν {λογ3} προσπάθειες')
                if λογ3 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
    else:
        print('Πάμε παρακάτω...')
def English_προσπάθειες():
    category3 = input('Αγγλικά ')
    if category3 == "Ναι" or category3 == "ναι" or category3 == "Yes" or category3 == "Nai" or category3 == "ΝΑΙ":
        print('\n')
        print("Για να σε δούμε...")
        print("Ερώτηση 1:")
        print('-'*10)
        engl1 = 2
        while engl1 > 0:
            print("Συμβιβάζομαι, Ανέχομαι, Φοράω κάτι")
            q1 = input("Τι σημαίνει η φράση put up with;")
            if q1 == 'Ανέχομαι' or q1 == 'ανέχομαι' or q1 == 'ΑΝΕΧΟΜΑΙ':
                print('Καλός και στα Αγγλικά!')
                engl1 -= 5
            else:
                print('Πάμε πάλι...')
                engl1 -= 1
                print(f'Σου απομένουν {engl1} προσπάθειες')
                if engl1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 2:")
        print('-'*10)
        engl2 = 2
        while engl2 > 0:    
            print("Come, Comed, Commes")
            q2 = input("Ποιό από τα παραπάνω είναι past participle του ρήματος come;")
            if q2 == "Come" or q2 == "come" or q2 == "COME" or q2 == "Ψομε":
                print("Μπράβοοο!")
                engl2 -= 5
            else:
                print('Κάποιος δεν ξέρει να ανώματα ρήματα στα αγγλικά... Πάμε πάλι')
                engl2 -= 1 
                print(f'Σου απομένουν {engl2} προσπάθειες')
                if engl2 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 3:")
        print('-'*10)
        engl3 = 2
        while engl3 > 0:
            print("Homemade, Handmade, Inmade")
            q3 = input("Ποιό από τα παραπάνω σημαίνει σπιτικός;")
            if q3 == "Homemade" or q3 == "homemade" or q3 == "HOMEMADE" or q3 == "Ηομεμαδε":
                print("Amazing!")
                engl3 -= 5
            else:
                print('No of course not! Try again please!')
                engl3 -= 1
                print(f'Σου απομένουν {engl3} προσπάθειες')
                if engl3 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
    else:
        print('Πάμε παρακάτω...')
def Μαθηματικά_προσπάθειες():
    category4 = input('Μαθηματικά ')
    if category4 == "Ναι" or category4 == "ναι" or category4 == 'ΝΑΙ':
        print('\n')
        print("Στις ερωτήσεις να απαντάς με 1, 2 και 3 αντίστοιχα.")
        print("Ερώτηση 1:")
        print('-'*10)
        math1 = 2
        while math1 > 0:
            print("α^2-2αβ-β^2, β^2-2αβ+α^2, α-2αβ^2+β^2")
            e = input("Ποιό είναι το ανάπτυγμα της ταυτότητας (α-β)^2 ")
            if e == "2" or e == "δύο":
                print("Πολύ σωστά!")
                math1 -= 5
            else:
                print('Μην σε μπερδεύει η λέξη ανάπτυγμα... απλά κάνε τη ταυτότητα όπως την ξέρεις!')
                math1 -= 1
                print(f'Σου απομένουν {math1} προσπάθειες')
                if math1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 2:")
        print('-'*10)
        math2 = 2
        while math2 > 0:
            print("α^2+β^3+γ^3+2αβγ, α^2+β^2+γ^2+2αβ+2αγ+2βγ, α^3+2αγ+γ^3+β^2")
            e1 = input("Ποιό είναι το ανάπτυγμα της ταυτότητας (α+β+γ)^2 ")
            if e1 == "2" or e1 == "δύο":
                print("Πολύ σωστά!")
                math2 -= 5
            else:
                print('Αν δε θυμάσαι πώς αναλύουμε τη ταυτότητα, κάνε πολλαπλασιασμό: (α+β+γ)*(α+β+γ)')
                math2 -= 1
                print(f'Σου απομένουν {math2} προσπάθειες')
                if math1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print("Ερώτηση 3:")
        print('-'*10)
        math3 = 2
        while math3 > 0:
            print("α^2, β^2+2αβ, 2αβ")
            e2 = input("Ποιό είναι το αποτέλεσμα: (α+β)^2-(α^2+β^2) ")
            if e2 == "3" or e2 == "τρία":
                print("Πολύ σωστά!")
                math3 -= 5
            else:
                print('Δε πειράζει πάμε ξανά!')
                math3 -= 1
                print(f'Σου απομένουν {math3} προσπάθειες')
                if math3 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
    else:
        print('Πάμε παρακάτω...')
def Φυσική_προσπάθειες():
    category5 = input('Φυσική ')
    if category5 == "Ναι" or category5 == "ναι" or category5 == 'ΝΑΙ':
        print('\n')
        print('Ερώτηση 1:')
        print('-'*10)
        phy1 = 2
        while phy1 > 0:
            print('1A, 1V, 1Ω, 1J, 1W')
            ph1 = input('Ποια μονάδα από τις παραπάνω θα χρησιμοποιούσες για να μετρήσεις την ισχύ ενός διπόλου;')
            if ph1 == '1W' or ph1 == '1w' or ph1 == 'W' or ph1 == '1w' or ph1 == '1Βατ':
                print('Μπράβο! Το 1W (ή ένα Βατ) είναι η μονάδα μέτρησης της Ισχύος στο Διεθνές Σύστημα Μονάδων (S.I.) και 1W = 1A * 1V')
                phy1 -= 5
            else:
                print('Για προσπάθησε άλλη μία φορά... μην σε μπερδέυει το ότι έχω βάλει πολλές μονάδες! Το 1J είναι ενέργεια!')
                phy1 -= 1
                print(f'Σου απομένουν {phy1} προσπάθειες')
                if ph1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print('Ερώτηση 2:')
        print('-'*10)
        phy2 = 2
        while phy2 > 0:
            print('Αμπερόμετρο, Βολτόμετρο, Ωμόμετρο, Πολύμετρο, Παλμογράφος')
            ph2 = input('Τα παραπάνω είναι όργανα μέτρησης. Ποιο από τα παραπάνω όργανα θα χρησιμοποιούσες για να μετρήσεις την Ισχύ ενός διπόλου;')
            if ph2 == 'Πολύμετρο' or ph2 == 'πολύμετρο' or ph2 == 'ΠΟΛΥΜΕΤΡΟ':
                print('Εύγε! Θα χρησμοποιούσες το πολύμετρο, το οποίο παρόλο που δε μετράει την ισχύ, αυτή καθ αυτή, μετράει και την ένταση του ηλ. ρεύματος και την τάση στα άκρα της συσκευής σου! Έτσι με τον παραπάνω τύπο (1W = 1A * 1V) Θα μπορέσεις να βρεις την ισχύ του διπόλου!')
                phy2 -= 5
            else:
                print('Σου φάνησε δύσκολη η ερώτηση(;) ... σε ρώτησα την ΙΣΧΥ!')
                phy2 -= 1
                print(f'Σου απομένουν {phy2} προσπάθειες')
                if ph2 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print('Ερώτηση 3:')
        print('-'*10)
        phy3 = 2
        while phy3 > 0:
            print('αντίστροφα, σε σειρά, παράλληλα, ανάστροφα')
            ph3 = input('Στο σπίτι σου έχεις λάμπες· σωστά; Ε λοιπόν, πώς πρέπει να συνδέσουμε τις λάμπες έτσι ώστε: όχι μόνο όταν καεί η μία να συνεχίσζουν να δουλεύουν οι υπόλοιπες, αλλά και να μην επηρεαστεί καθόλου το πόσο έντονα θα φωτοβολούν οι λάμπες στη περίπτωση που καεί η μία;')
            if ph3 == 'παράλληλα' or ph3 == 'Παράλληλα' or ph3 == 'ΠΑΡΑΛΛΗΛΑ':
                print('Μπράβοο! Εμείς ξέρουμε ότι όταν συνδέεις αντιστάτες παράλληλα, έχουν την ίδια τάση και όταν κλείσουμε έναν αντιστάτη οι υπόλοιποι που είναι συνδεδεμένοι παράλληλα θα έχουν ακριβώς την ίδια ένταση με προηγουμένως! Άρα, οι λάμπες θα φωτοβολούν το ίδιο.')
                phy3 -= 5
            else:
                print('Για προσπάθησε ξανά! Μην σε μπερδεύουν οι λάμπες, σκέψου τα Χριστουγεννιάτικα λαμπάκια που βάζουμε στο δέντρο!')
                phy3 -= 1
                print(f'Σου απομένουν {phy3} προσπάθειες')
                if ph3 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
    else:
        print('Πάμε παρακάτω...')
def Χημεία_προσπάθειες():
    category6 = input('Χημεία ')
    if category6 == "Ναι" or category6 == "ναι" or category6 == 'ΝΑΙ':
        print('\n')
        print('Ερώτηση 1:')
        print('-'*10)
        chem1 = 2
        while chem1 > 0:
            print('Νερό, Αλάτι, Διοξείδιο του άνθρακα, Τίποτα')
            che1 = input('Τι θα σχηματιστεί αν ανακατέψουμε σόδα με ξίδι;')  
            if che1 == 'Αλάτι' or che1 == 'αλάτι' or che1 == 'ΑΛΑΤΙ':
                print('Εύγε! Θα σχηματιστούν κρύσταλοι άλατος!')
                chem1 -= 5
            else:
                print('Πολύ απλή ερώτηση νομίζω! Το Τίποτα το αποκλύουμε γιατί και τα δύο είναι χημικά συστατικά... θα σχηματιστεί προφανώς μια χημική ένωση! Πάμε πάλι!')
                chem1 -= 1
                print(f'Σου απομένουν {chem1} προσπάθειες')
                if chem1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print('Ερώτηση 2:')
        print('-'*10)
        chem2 = 2
        while chem2 > 0:
            print('2, 8, 4, 6, 16')
            che2 = input('Ο ατομικός αριθμός του οξυγόνου είναι 8, πόσα ηλεκτρόνια έχει ένα μόριο οξυγόνου;')
            if che2 == '8':
                print('Πολύ σωστά! Έχει 8 ηλεκτρόνια και 8 πρωτόνια!')
                chem2 -= 5
            else:
                print('Για προσπάθησε ξανά... ο ατομικός αριθμός είναι Z και ο αριθμός των νετρονίων είναι Ν... για θυμίσου!')
                chem2 -= 1
                print(f'Σου απομένουν {chem2} προσπάθειες')
                if chem2 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print('Ερώτηση 3:')
        print('-'*10)
        chem3 = 2
        while chem3 > 0:
            print('ανιόν υδρογόνου, κατιόν υδρογόνου, πανιόν υδρογόνου')
            che3 = input('Ένα ιόν υδρογόνου έχει -3 ηλεκτόνια. Πώς ονομάζεται;')
            if che3 == "κατιόν υδρογόνου" or che3 == "Κατιόν Υδρογόνου" or che3 == "ΚΑΤΙΟΝ ΥΔΡΟΓΟΝΟΥ":
                print('Μπραβίσιμο!')
                chem3 -= 5
            else:
                print('Δεν υπάρχει το πανιόν... για ξαναδες το τώρα')
                chem3 -= 1
                print(f'Σου απομένουν {chem3} προσπάθειες')
                if chem3 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
def Ιστορία_προσπάθειες():
    category7 = input('Ιστορία ')
    if category7 == "Ναι" or category7 == "ναι" or category7 == 'ΝΑΙ':
        print('\n')
        print('Ερώτηση 1:')
        print('-'*10)
        hist1 = 3
        while hist1 > 0:
            print('1435, 1453, 1776, 1467, 1978, 1987')
            his1 = input('Η πρώτη άλωση της Κωνσταντινούπολης έγινε το... ')
            if his1 == '1453' or his1 == 'το 1453':
                print('Εύγε! Το 1453 έγινε!')
                hist1 -= 5
            else:
                print('Να θυμάσαι ότι έγινε τον 15ο αιώνα μ.Χ. Προσπάθησε πάλι!')
                hist1 -= 1
                print(f'Σου απομένουν {hist1} προσπάθειες')
                if hist1 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    global pl
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print('Ερώτηση 2:')
        print('-'*10)
        hist2 = 2
        while hist2 > 0:
            print('Ναι, Όχι, Ονομάζεται αλλιώς')
            his2 = input('Ο 1ος Παγκόσμιος Πόλεμος ονομάζεται και πόλεμος των Χαρακωμάτων;')
            if his2 == 'Ναι'or his2 == 'ναι' or his2 == 'ΝΑΙ':
                print('Μπράβο διαβασμένος σε βλέπω!')
                hist2 -= 5
            else:
                print('Κάποιος είναι λίγο αδιάβαστος βλέπω... Προσπάθησε ξανά!')
                hist2 -= 1
                print(f'Σου απομένουν {hist2} προσπάθειες')
                if hist2 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')
                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
        print('\n')
        print('Ερώτηση 3:')
        print('-'*10)
        hist3 = 2
        while hist3 > 0:
            print('με την εισοβολή του Μουσολίνι στην Αθήνα, με την εισοβολή του Χίτρελ στη Ρωσία, με την εισβολή του Μουσολίνι στα Ιεροσόλυμα, με την εισβολή του Χίτρελ στη Πολωνία')
            his3 = input('Ο 2ος παγκόσμιος πόλεμος άρχισε με... (απάντα με 1 ή 2 ή 3 ή 4)')
            if his3 == '4':
                print('Ωραίος ο νέος!')
                hist3 -= 5
            else:
                print('Πληροφοριακά άρχισε στην Ευρώπη και εξαπλώθηκε σε όλη την οικουμένη αργότερα! Προσπάθησε άλλη μία φορά!')
                hist3 -= 1
                print(f'Σου απομένουν {hist3} προσπάθειες')
                if hist3 <= 0:
                    print('Χάσατε... προσπαθήστε ξανά')

                    pl += 1
                    break
        print('-' * 5)
        print(f'Έχεις {pl} λάθος απαντήσεις')
        print('-' * 5)
    else:
        print('Πάμε παρακάτω...')
def Ολα_χωρίς_προσπάθειες():
    ξανά = input('Θέλεις να ξανακάνεις κάποια ερωτηση; (Ναι ή Όχι)')
    if ξανά == 'Ναι' or ξανά == 'ναι' or ξανά == 'NAI'or ξανά == 'ΝΑι':
        print('ok...')
        category = input("Διάλεξε μια κατηγορία στην οποία θες να τεστάρεις τις γνώσεις σου: (Πληροφορική, Αγγλικά,Γλώσσα - Λογοτεχνία, Ιστορία, Μαθηματικά, Φυσική ή Χημέια: ")
        if category == "Πληροφορική" or category == "πληροφορική" or category == "ΠΛΗΡΟΦΟΡΙΚΗ":
            print('\n')
            print("Ερώτηση 1:")
            print('-'*10)
            πληρ1 = True
            while πληρ1:
                print("CPU, GPU, SSD, HDD ή USB;")
                qu1 = input("Πως λέγεται σε συντομογραφία η κάρτα γραφικών; ")
                if qu1 == 'GPU'or qu1 == 'gpu'or qu1 == 'G.P.U.':
                    print('Μπράβο το G.P.U. είναι το Graphics processing unit, δηλαδή εκεί που επεξεργάζονται τα γραφικά, αυτό που βλέπεις στην οθόνη!')
                    πληρ1 = False
                else:
                    print('Μια μικρή βοήθεια: όπου βλέπεις D στο τέλος μιας λέξης από τις παραπάνω είναι Disk (δίσκος)...')
            print("Ερώτηση 2:")
            print('-'*10)
            πληρ2 = True
            while πληρ2:
                print("Word, Notepad, Pages, OpenOffice, Libre Writer")
                qu2 = input("Ποιά από τις παραπάνω είναι εφαρμογή της Microsoft; ")
                if qu2 == 'Word' or qu2 == 'word'or qu2 == 'WORD':
                    print('Καλός καλός! Έτσι πληροφοριακά όλα τα παραπάνω προγράμματα είναι για επεξεργασία κειμένου, αλλά μόνο το Word είναι της Microsoft.')
                    πληρ2 = False
                else:
                    print('Δε νομίζω πως είναι δύσκολο... μια μικρή βοήθεια το Pages δεν είναι πρόγραμμα των windows, είναι εφαρμογή της Apple.')
            print("Ερώτηση 3:")
            print('-'*10)
            πληρ3 = True
            while πληρ3:
                print("Intel, AMD, Apple, NVidia")
                qu3 = input("Ποιά από τις παραπάνω ΔΕΝ είναι μάρκα επεξεργαστών;")
                if qu3 == "NVidia" or qu3 == "nvidia" or qu3 == "NVIDIA":
                    print("Πολύ σωστά, η NVidia είναι η πιο γνωστή εταιρεία που παράγει κάρτες γραφικών(GPU).")
                    πληρ3 = False
                else:
                    print('Λίγο ανεβάσαμε τον πήχη; Δεν μιλάω συγκεκριμένα για επεξεργαστές υπολογιστών... και τα κινητά τηλέφωνα (π.χ.) έχουν επεξεργαστή!')
        elif category == "Γλώσσα - Λογοτεχνία" or category == "Γλώσσα-Λογοτεχνία" or category == "γλώσσα - λογοτεχνία" or category == "γλώσσα-λογοτεχνία" or category == "Γλώσσα Λογοτεχνία" or category == "γλώσσα λογοτεχνία":
            print("Ερώτηση 1:")
            print('-'*10)
            λογ1 = True
            while λογ1:
                print("Φεραίος, Κορνάρος, Ελύτης")
                que1 = input("Ποιός έγραψε τον Θούριο;")
                if que1 == "Φεραίος" or que1 == "Φερέος" or que1 == "φεραίος" or que1 == "ΦΕΡΑΙΟΣ":
                    print("Δεν έχω λόγια!!!")
                    λογ1 = False
                else:
                    print('Προσπάθησε ξανά... απλά να ξέρεις ο Οδ. Ελύτης ήταν ένας από τους πιο σπουδαίους ποιητές της Ελλάδας!')
            print("Ερώτηση 2")
            print('-'*10)
            λογ2 = True
            while λογ2:
                print("Αντίθεση, Eιρωνεία, Έλλειψη")
                que2 = input("Ποιό σχήμα λόγου παρατηρείτε στο παράδειγμα: Ωραία τα κατάφερες!")
                if que2 == 'Ειρωνεία' or que2 == 'ειρωνεία' or que2 == 'ΕΙΡΩΝΕΙΑ' or que2 == 'Ειρονεία':
                    print('Πολύ καλός παίχτης! Αν το βρήκες με τη πρώτη Μπράβο, αλλιώς δε πειράζει έμαθες...')
                    λογ2 = False
                else:
                    print('Μήπως εσύ έχεις έλλειψη; Για δες ξανά φίλε μου! (ΑΝΤΙΘΕΣΗ)')
            print("Ερώτηση 3")
            print('-'*10)
            λογ3 = True
            while λογ3:
                print("Παραγράφους, Ομοιοκαταληξίες ή Στροφές")
                ques1 = input("Το ποίημα έχει πάντα...")
                if ques1 == 'Στροφές'or ques1 == 'στροφές' or ques1 == 'Στροφες':
                    print('Το βρήκες! Ομοιοκαταληξίες δεν έχουν όλα τα ποιήματα, ειδικότερα αν ανήκουν στη μοντέρνα ποίηση!')
                    λογ3 = False
                else:
                    print('Σε ρώτησα συγκεκριμένα τι έχει ένα ποίημα ΠΑΝΤΑ... εκ φύσεως πώς το λένε; Ξανά!')
        elif category == "Αγγλικά" or category == "αγγλικά" or category == "ΑΓΓΛΙΚΑ" or category == "English":
            print("Για να σε δούμε...")
            print("Ερώτηση 1:")
            print('-'*10)
            engl1 = True
            while engl1:
                print("Συμβιβάζομαι, Ανέχομαι, Φοράω κάτι")
                q1 = input("Τι σημαίνει η φράση put up with;")
                if q1 == 'Ανέχομαι' or q1 == 'ανέχομαι' or q1 == 'ΑΝΕΧΟΜΑΙ':
                    print('Καλός και στα Αγγλικά!')
                    engl1 = False
                else:
                    print('Πάμε πάλι...')
            print("Ερώτηση 2:")
            print('-'*10)
            engl2 = True
            while engl2:    
                print("Come, Comed, Commes")
                q2 = input("Ποιό από τα παραπάνω είναι past participle του ρήματος come;")
                if q2 == "Come" or q2 == "come" or q2 == "COME" or q2 == "Ψομε":
                    print("Μπράβοοο!")
                    engl2 = False
                else:
                    print('Κάποιος δεν ξέρει να ανώματα ρήματα στα αγγλικά... Πάμε πάλι')
            print("Ερώτηση 3:")
            print('-'*10)
            engl3 = True
            while engl3:
                print("Homemade, Handmade, Inmade")
                q3 = input("Ποιό από τα παραπάνω σημαίνει σπιτικός;")
                if q3 == "Homemade" or q3 == "homemade" or q3 == "HOMEMADE" or q3 == "Ηομεμαδε":
                    print("Amazing!")
                    engl3 = False
                else:
                    print('No of course not! Try again please!')
        elif category == "Μαθηματικά" or category == "μαθηματικά" or category == "ΜΑΘΗΜΑΤΙΚΑ":
            print("Στις ερωτήσεις να απαντάς με 1, 2 και 3 αντίστοιχα.")
            print("Ερώτηση 1:")
            print('-'*10)
            math1 = True
            while math1:
                print("α^2-2αβ-β^2, β^2-2αβ+α^2, α-2αβ^2+β^2")
                e = input("Ποιό είναι το ανάπτυγμα της ταυτότητας (α-β)^2")
                if e == "2" or e == "δύο":
                    print("Πολύ σωστά!")
                    math1 = False
                else:
                    print('Μην σε μπερδεύει η λέξη ανάπτυγμα... απλά κάνε τη ταυτότητα όπως την ξέρεις!')
            print("Ερώτηση 2:")
            print('-'*10)
            math2 = True
            while math2:
                print("α^2+β^3+γ^3+2αβγ, α^2+β^2+γ^2+2αβ+2αγ+2βγ, α^3+2αγ+γ^3+β^2")
                e1 = input("Ποιό είναι το ανάπτυγμα της ταυτότητας (α+β+γ)^2")
                if e1 == "2" or e1 == "δύο":
                    print("Πολύ σωστά!")
                    math2 = False
                else:
                    print('Αν δε θυμάσαι πώς αναλύουμε τη ταυτότητα, κάνε πολλαπλασιασμό: (α+β+γ)*(α+β+γ)')
            print("Ερώτηση 3:")
            print('-'*10)
            math3 = True
            while math3:
                print("α^2, β^2+2αβ, 2αβ")
            e2 = input("Ποιό είναι το αποτέλεσμα: (α+β)^2-(α^2+β^2)")
            if e2 == "3" or e2 == "τρία":
                print("Πολύ σωστά!")
                math3 = False
            else:
                print('Δε πειράζει πάμε ξανά!')
        elif category == 'Φυσική' or category == 'φυσική' or category == 'ΦΥΣΙΚΗ':
            print('Ερώτηση 1:')
            print('-'*10)
            phy1 = True
            while phy1:
                print('1A, 1V, 1Ω, 1J, 1W')
                ph1 = input('Ποια μονάδα από τις παραπάνω θα χρησιμοποιούσες για να μετρήσεις την ισχύ ενός διπόλου;')
                if ph1 == '1W' or ph1 == '1w' or ph1 == 'W' or ph1 == '1w' or ph1 == '1Βατ':
                    print('Μπράβο! Το 1W (ή ένα Βατ) είναι η μονάδα μέτρησης της Ισχύος στο Διεθνές Σύστημα Μονάδων (S.I.) και 1W = 1A * 1V')
                    phy1 = False
                else:
                    print('Για προσπάθησε άλλη μία φορά... μην σε μπερδέυει το ότι έχω βάλει πολλές μονάδες! Το 1J είναι ενέργεια!')
            print('Ερώτηση 2:')
            print('-'*10)
            phy2 = True
            while phy2:
                print('Αμπερόμετρο, Βολτόμετρο, Ωμόμετρο, Πολύμετρο, Παλμογράφος')
                ph2 = input('Τα παραπάνω είναι όργανα μέτρησης. Ποιο από τα παραπάνω όργανα θα χρησιμοποιούσες για να μετρήσεις την Ισχύ ενός διπόλου;')
                if ph2 == 'Πολύμετρο' or ph2 == 'πολύμετρο' or ph2 == 'ΠΟΛΥΜΕΤΡΟ':
                    print('Εύγε! Θα χρησμοποιούσες το πολύμετρο, το οποίο παρόλο που δε μετράει την ισχύ, αυτή καθ αυτή, μετράει και την ένταση του ηλ. ρεύματος και την τάση στα άκρα της συσκευής σου! Έτσι με τον παραπάνω τύπο (1W = 1A * 1V) Θα μπορέσεις να βρεις την ισχύ του διπόλου!')
                    phy2 = False
                else:
                    print('Σου φάνησε δύσκολη η ερώτηση(;) ... σε ρώτησα την ΙΣΧΥ!')
            print('Ερώτηση 3:')
            print('-'*10)
            phy3 = True 
            while phy3:
                print('αντίστροφα, σε σειρά, παράλληλα, ανάστροφα')
                ph3 = input('Στο σπίτι σου έχεις λάμπες· σωστά; Ε λοιπόν, πώς πρέπει να συνδέσουμε τις λάμπες έτσι ώστε: όχι μόνο όταν καεί η μία να συνεχίσζουν να δουλεύουν οι υπόλοιπες, αλλά και να μην επηρεαστεί καθόλου το πόσο έντονα θα φωτοβολούν οι λάμπες στη περίπτωση που καεί η μία;')
                if ph3 == 'παράλληλα' or ph3 == 'Παράλληλα' or ph3 == 'ΠΑΡΑΛΛΗΛΑ':
                    print('Μπράβοο! Εμείς ξέρουμε ότι όταν συνδέεις αντιστάτες παράλληλα, έχουν την ίδια τάση και όταν κλείσουμε έναν αντιστάτη οι υπόλοιποι που είναι συνδεδεμένοι παράλληλα θα έχουν ακριβώς την ίδια ένταση με προηγουμένως! Άρα, οι λάμπες θα φωτοβολούν το ίδιο.')
                    phy3 = False
                else:
                    print('Για προσπάθησε ξανά! Μην σε μπερδεύουν οι λάμπες, σκέψου τα Χριστουγεννιάτικα λαμπάκια που βάζουμε στο δέντρο!')
        elif category == 'Χημεία' or category == 'χημεία' or category == 'ΧΗΜΕΙΑ':
            print('Ερώτηση 1:')
            print('-'*10)
            chem1 = True
            while chem1:
                print('Νερό, Αλάτι, Διοξείδιο του άνθρακα, Τίποτα')
                che1 = input('Τι θα σχηματιστεί αν ανακατέψουμε σόδα με ξίδι;')  
                if che1 == 'Αλάτι' or che1 == 'αλάτι' or che1 == 'ΑΛΑΤΙ':
                    print('Εύγε! Θα σχηματιστούν κρύσταλοι άλατος!')
                    chem1 = False
                else:
                    print('Πολύ απλή ερώτηση νομίζω! Το Τίποτα το αποκλύουμε γιατί και τα δύο είναι χημικά συστατικά... θα σχηματιστεί προφανώς μια χημική ένωση! Πάμε πάλι!')
            print('Ερώτηση 2:')
            print('-'*10)
            chem2 = True
            while chem2:
                print('2, 8, 4, 6, 16')
                che2 = input('Ο ατομικός αριθμός του οξυγόνου είναι 8, πόσα ηλεκτρόνια έχει ένα μόριο οξυγόνου;')
                if che2 == '8':
                    print('Πολύ σωστά! Έχει 8 ηλεκτρόνια και 8 πρωτόνια!')
                    chem2 = False
                else:
                    print('Για προσπάθησε ξανά... ο ατομικός αριθμός είναι Z και ο αριθμός των νετρονίων είναι Ν... για θυμίσου!')
            print('Ερώτηση 3:')
            print('-'*10)
            chem3 = True
            while chem3:
                print('ανιόν υδρογόνου, κατιόν υδρογόνου, πανιόν υδρογόνου')
                che3 = input('Ένα ιόν υδρογόνου έχει -3 ηλεκτόνια. Πώς ονομάζεται;')
                if che3 == "κατιόν υδρογόνου" or che3 == "Κατιόν Υδρογόνου" or che3 == "ΚΑΤΙΟΝ ΥΔΡΟΓΟΝΟΥ":
                    print('Μπραβίσιμο!')
                    chem3 = False
                else:
                    print('Δεν υπάρχει το πανιόν... για ξαναδες το τώρα')
        elif category == 'Ιστορία' or category == 'ιστορία' or category == 'ΙΣΤΟΡΙΑ':
            print('Ερώτηση 1:')
            print('-'*10)
            hist1 = True
            while hist1:
                print('1435, 1453, 1776, 1467, 1978, 1987')
                his1 = input('Η πρώτη άλωση της Κωνσταντινούπολης έγινε το... ')
                if his1 == '1453':
                    print('Εύγε! Το 1453 έγινε!')
                else:
                    print('Να θυμάσαι ότι έγινε τον 15ο αιώνα μ.Χ. Προσπάθησε πάλι!')
                    hist1 = False
                    print(f'Σου απομένουν {hist1} προσπάθειες')
            print('Ερώτηση 2:')
            print('-'*10)
            hist2 = True
            while hist2:
                print('Ναι, Όχι, Ονομάζεται αλλιώς')
                his2 = input('Ο 1ος Παγκόσμιος Πόλεμος ονομάζεται και πόλεμος των Χαρακωμάτων;')
                if his2 == 'Ναι'or his2 == 'ναι' or his2 == 'ΝΑΙ':
                    print('Μπράβο διαβασμένος σε βλέπω!')
                else:
                    print('Κάποιος είναι λίγο αδιάβαστος βλέπω... Προσπάθησε ξανά!')
                    hist2 = False
                    print(f'Σου απομένουν {hist2} προσπάθειες')
            print('Ερώτηση 3:')
            print('-'*10)
            hist3 = True
            while hist3:
                print('με την εισοβολή του Μουσολίνι στην Αθήνα, με την εισοβολή του Χίτρελ στη Ρωσία, με την εισβολή του Μουσολίνι στα Ιεροσόλυμα, με την εισβολή του Χίτρελ στη Πολωνία')
                his3 = input('Ο 2ος παγκόσμιος πόλεμος άρχισε με... (απάντα με 1 ή 2 ή 3 ή 4)')
                if his3 == '4':
                    print('Ωραίος ο νέος!')
                    hist3 = False
                else:
                    print('Πληροφοριακά άρχισε στην Ευρώπη και εξαπλώθηκε σε όλη την οικουμένη αργότερα! Προσπάθησε άλλη μία φορά!')
        else:
            τέλος()
def τέλος():
    global pl

    if pl >= 9:
        print('=' * 12)
        print('Έχασες! Προσπάθησε ξανά!')
        print('\n')
    else:
        print('=' * 12)
        print('Νίκησες! Μπράβο!')
        print('\n')

        print("Ευχαριστώ πολύ που αφιέρωσες λίγο χρόνο στο προγραμματάκι μας Θοδωρής Βασιλικός και Νίκος Καλλίτσης")
        print("Καλή συνέχεια!")

    exit1 = input('Πατα οποιοδήποτε κουμπί για να κλείσεις το πρόγραμμα')
    if exit1 == 'όχι δε θέλω':
        print('Ε τότε κάτσε εδώ')
        for i in range(15):
            print('...')
        print('Τι ακόμα δεν έφυγες')
    else:
        exit()
def τέλος_1():

    print("Ευχαριστώ πολύ που αφιέρωσες λίγο χρόνο στο προγραμματάκι μας Θοδωρής Βασιλικός και Νίκος Καλλίτσης")
    print("Καλή συνέχεια!")
    exit2 = input('Πατα οποιοδήποτε κουμπί για να κλείσεις το πρόγραμμα')

    if exit2 == 'όχι δε θέλω':
        print('Ε τότε κάτσε εδώ')
        for i in range(15):
            print('...')
        print('Τι ακόμα δεν έφυγες')
    else:
        exit()

# το κύριο πρόγραμμα:
print( "Γεια σου, αυτό είναι ένα παιχνίδι για να τεστάρεις τις γνώσεις σου σε διάφορα πραγματα που είναι χρήσιμα για "
       "το μέλλον σου" )
question = input("Θα ήθελες να συνεχίσεις (Ναι ή Όχι)  -> ")
if question == "Ναι" or question == 'ναι' or question == 'ΝΑΙ':
    print("τέλεια!")
    print("Διαλέγεις τις παρακάτω κατηγορίες απαντώντας Ναι ή Όχι:")
    Πληροφορική_προσπάθειες()
    English_προσπάθειες()
    Γλώσσα_Λογοτεχνία_προσπάθειες()
    Ιστορία_προσπάθειες()
    Μαθηματικά_προσπάθειες()
    Φυσική_προσπάθειες()
    Χημεία_προσπάθειες()
    Ολα_χωρίς_προσπάθειες()

else:
    τέλος_1()
