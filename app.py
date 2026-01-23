from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")

# --- DATA KRIPTOGRAFI (Dari Kode Anda) ---
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890-,.!@#$%^&*()=+?"

encrypt_8 = [
    "0HIKeDe1","0HSKhKe7","0HIElEg2","1HSCyDe3","0HIApDi3","0HSAgMn9","0HIEdGo4","0HSHePh5","0HIViHe5","0HSTrJa1",
    "0HIKaDe6","1HSMyNi0","0HISuBo7","0HSAnCe8","0HISaSe8","1HSCaTh1","0HIKoDa9","0HSDaGe4","1HIMoIn0","0HSCeTa2",
    "1HIGrSt1","0HSHyAq6","1HIHuVi2","0HSEvOr3","1HIPaRe3","1HSCiZa2","/07-KhKe","/13-CyDe","/09-AgMn","/05-HePh",
    "/01-TrJa","/10-MyNi","/08-AnCe","/11-CaTh","/04-DaGe","/02-CeTa","/06-HyAq","/03-EvOr","/12-CiZa","/01-KeDe",
    "/02-ElEg","/03-ApDi","/04-EdGo","/05-ViHe","/06-KaDe","/07-SuBo","/08-SaSe","/09-KoDa","/10-MoIn","/11-GrSt",
    "/12-HuVi","/13-PaRe"
]

encrypt_full = [
    "HIKeDeI","HSKhKe7","HIElEgII","1HSCyDe3","HIApDiIII","HSAgMn9","HIEdGoIV","HSHePh5","HIViHeV","HSTrJa1",
    "HIKaDeVI","1HSMyNi0","HISuBoVII","HSAnCe8","HISaSeVIII","1HSCaTh1","HIKoDaIX","HSDaGe4","HIMoInX","HSCeTa2",
    "XHIGrStI","HSHyAq6","XHIHuViII","HSEvOr3","XHIPaReIII","1HSCiZa2","/7-KhKe","/13-CyDe","/9-AgMn","/5-HePh",
    "/1-TrJa","/10-MyNi","/8-AnCe","/11-CaTh","/4-DaGe","/2-CeTa","/6-HyAq","/3-EvOr","/12-CiZa","/I-KeDe",
    "/II-ElEg","/III-ApDi","/IV-EdGo","/V-ViHe","/VI-KaDe","/VII-SuBo","/VIII-SaSe","/IX-KoDa","/X-MoIn","/XI-GrSt",
    "/XII-HuVi","/XIII-PaRe"
]

encrypt_short = [
    "KE","KH","EL","CY","AP","AG","ED","HE","VI","TR","KA","MY","SU","AN","SA","CA","KO","DA","MO","CE",
    "GR","HY","HU","EV","PA","CI","07","13","09","05","01","10","08","11","04","02","06","03","12","I",
    "II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII"
]

enigma_lists = [
    ["HIKeDeI","HSKhKe7","HIElEgII","1HSCyDe3","HIApDiIII","HSAgMn9","HIEdGoIV","HSHePh5","HIViHeV","HSTrJa1","HIKaDeVI","1HSMyNi0","HISuBoVII","HSAnCe8","HISaSeVIII","1HSCaTh1","HIKoDaIX","HSDaGe4","HIMoInX","HSCeTa2","XHIGrStI","HSHyAq6","XHIHuViII","HSEvOr3","XHIPaReIII","1HSCiZa2","/7-KhKe","/13-CyDe","/9-AgMn","/5-HePh","/1-TrJa","/10-MyNi","/8-AnCe","/11-CaTh","/4-DaGe","/2-CeTa","/6-HyAq","/3-EvOr","/12-CiZa","/I-KeDe","/II-ElEg","/III-ApDi","/IV-EdGo","/V-ViHe","/VI-KaDe","/VII-SuBo","/VIII-SaSe","/IX-KoDa","/X-MoIn","/XI-GrSt","/XII-HuVi","/XIII-PaRe"],
    ["KeDeHII","KhKeHS7","ElEgHIII","1CyDeHS3","ApDiHIIII","AgMnHS9","EdGoHIIV","HePhHS5","ViHeHIV","TrHaHS1","KaDeHIVI","1MyNiHS0","SuBoHIVII","AnCeHS8","SaSeHIVIII","1CaThHS1","KoDaHIIX","DaGeHS4","MoInHIX","CeTaHS2","XGrStIHII","HyAqHS6","XHuViHII","EvOrHS3","XPaReHIIII","1CiZaHS2","KhKe/-7","CyDe/-13","AgMn/-9","HePh/-5","TrJa/-1","MyNi/-10","AnCe/-8","CaTh/-11","DaGe/-4","CeTa/-2","HyAq/-6","EvOr/-3","CiZa/-12","KeDe/-I","ElEg/-II","ApDi/-III","EdGo/-IV","ViHe/-V","KaDe/-VI","SuBo/-VII","SaSe/-VIII","KoDa/-IX","MoIn/-X","GrSt/-XI","HuVi/-XII","PaRe/-XIII"],
    ["KeHIDeI","KhHSKe7","ElHIEgII","1CyHSDe3","ApHIDiIII","AgHSMn9","EdHIGoIV","HeHSPh5","ViHIHeV","TrHSHa1","DeHIKaVI","1MyHSNi0","SuHIBoVII","AnHSCe8","SaHISeVIII","1CaHSTh1","KoHIDaIX","DaHSGe4","MoHIInX","CeHSTa2","XGrHIStI","HyHSAq6","XHuHIViII","EvHSOr3","XPaHIReIII","1CiHSZa2","Kh-7/Ke","Cy-13/De","Ag-9/Mn","He-5/Ph","Tr-1/Ja","My-10/Ni","An-8/Ce","Ca-11/Th","Da-4/Ge","Ce-2/Ta","Hy-6/Aq","Ev-3/Or","Ci-12/Za","Ke-I/De","El-II/Eg","Ap-III/Di","Ed-IV/Go","Vi-V/He","Ka-VI/De","Su-VII/Bo","Sa-VIII/Se","Ko-IX/Da","Mo-X/In","Gr-XI/St","Hu-XII/Vi","Pa-XIII/Re"],
    ["DeHIKeI","KeHSKh","EgHIElII","1DeHSCy3","DiHIApIII","MnHSAg9","GoHIEdIV","PhHSHe5","HeHIViV","HaHSTr1","KaHIDeVI","1NiHSMy0","BoHISuVII","CeHSAn8","SeHISaVIII","1ThHSCa1","DaHIKoIX","GeHSDa4","InHIMoX","TaHSCe2","XStHIGrI","AqHSHy6","XViHIHuII","OrHSEv3","XReHIPaIII","1ZaHSCi2","Ke/-7Kh","De/-13Cy","Mn/-9Ag","Ph/-5He","Ja/-1Ja","Ni/-10My","Ce/-8An","Th/-11Ca","Ge/-4Da","Ta/-2Ce","Aq/-6Hy","Or/-3Ev","Za/-12Ci","De/-IKe","Eg/-IIEl","Di/-IIIAp","Go/-IVEd","He/-VVi","De/-VIKa","Bo/-VIISu","Se/-VIIISa","Da/-IXKo","In/-XMo","St/-XIGr","Vi/-XIIHu","Re/-XIIIPa"]
]

enigma_patterns = {
    "1": [1,2,3,4], "2": [1,2,3,4,3,2,1], "3": [1,4,2,3], "4": [3,1,2,4], "5": [3,4,1,2],
    "6": [4,3,2,1,4,3,2,1], "7": [4,3,2,1,2,3,4], "8": [1,3,2,4], "9": [2,4,1,3], "10": [2,3,4,1]
}

# --- LOGIKA CORE ---
def encrypt_logic(text, mode, enigma_p=None):
    result = ""
    if mode == "4":
        counter = {c: 0 for c in alphabet}
        pattern = enigma_patterns.get(enigma_p, [1,2,3,4])
        for c in text.lower():
            if c in alphabet:
                idx = alphabet.index(c)
                p = counter[c] % len(pattern)
                version = pattern[p] - 1
                result += enigma_lists[version][idx]
                counter[c] += 1
    else:
        for char in text.lower():
            if char == " ": continue
            if char in alphabet:
                idx = alphabet.index(char)
                if mode == "1": result += encrypt_8[idx]
                elif mode == "2": result += encrypt_full[idx]
                elif mode == "3": result += encrypt_short[idx]
    return result

def decrypt_logic(text, mode, enigma_p=None):
    result = ""
    if mode == "1":
        for i in range(0, len(text), 8):
            block = text[i:i+8]
            if block in encrypt_8: result += alphabet[encrypt_8.index(block)]
    elif mode == "3":
        # Perbaikan logika decrypt singkat: mencocokkan token di list
        i = 0
        while i < len(text):
            matched = False
            for idx, token in enumerate(encrypt_short):
                if text.startswith(token, i):
                    result += alphabet[idx]
                    i += len(token)
                    matched = True; break
            if not matched: i += 1
    elif mode == "2":
        i = 0
        while i < len(text):
            matched = False
            for idx, token in enumerate(encrypt_full):
                if text.startswith(token, i):
                    result += alphabet[idx]
                    i += len(token)
                    matched = True; break
            if not matched: i += 1
    elif mode == "4":
        counter = {c: 0 for c in alphabet}
        pattern = enigma_patterns.get(enigma_p, [1,2,3,4])
        i = 0
        while i < len(text):
            matched = False
            for c in alphabet:
                idx = alphabet.index(c)
                p = counter[c] % len(pattern)
                version = pattern[p] - 1
                token = enigma_lists[version][idx]
                if text.startswith(token, i):
                    result += c
                    counter[c] += 1
                    i += len(token)
                    matched = True; break
            if not matched: i += 1
    return result

# --- ROUTES ---
@app.route("/")
def home():
    return render_template('index.html', patterns=enigma_patterns)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    action = data.get('action') # 'encrypt' or 'decrypt'
    mode = data.get('mode')
    text = data.get('text')
    enigma_p = data.get('enigma_p')

    if action == 'encrypt':
        res = encrypt_logic(text, mode, enigma_p)
    else:
        res = decrypt_logic(text, mode, enigma_p)
    
    return jsonify({'result': res})

if __name__ == '__main__':
    app.run(debug=True)