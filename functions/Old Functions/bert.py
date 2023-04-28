from transformers import AutoModel, AutoTokenizer, BartForConditionalGeneration, pipeline
import torch


def BRT(prompt):
    answerer_model = "KBLab/bert-base-swedish-cased-squad-experimental"  # Swedish BERT model
    mask_model = "KBLab/bart-base-swedish-cased"  # Swedish BART model

    # Use pipeline to produce an answerer from BERT
    answerer = pipeline("question-answering",
                        model=answerer_model, tokenizer=answerer_model)

    doc = "Jorden är den tredje planeten från solen och den största av de så kallade stenplaneterna i solsystemet. Jorden är hemvist för alla kända levande varelser, inklusive människan. Dess latinska namn, Tellus eller Terra, används ibland om den, och astronomer betecknar den ibland med symbolen 🜨 (solkors) eller ♁ (riksäpple). Jorden har en naturlig satellit kallad månen, eller Luna på latin. Med flera miljoner arter är jorden den enda himlakropp där man vet att liv existerar. Planeten bildades för 4,54 miljarder år sedan och liv uppstod inom en miljard år därefter (äldsta tecken på liv är ett kol-lager 3,8 miljarder år gammalt, äldsta säkra spår av celler är stromatoliter 3,5 miljarder år gamla)[11]. Sedan dess har jordens biosfär markant förändrat atmosfären och andra icke biologiska förhållanden, vilket till exempel tillåtit aerobiska organismer att utvecklas i den syrerika miljön. Sedd från rymden är jorden formad som ett nästan perfekt klot. Cirka 70 procent av ytan är täckt av hav med saltvatten; återstoden består av öar och kontinenter. Jordens inre är fortsatt aktiv med en relativt fast mantel, en flytande yttre kärna som genererar ett magnetfält, samt en fast inre kärna främst bestående av järn. Jordskorpan, jordens yttre lager, är uppdelad i en rad olika segment, kallade kontinentalplattor, som långsamt rör sig över ytan. Jorden har en atmosfär som till största delen består av kväve 78 % och syre 21 %. Jorden samverkar genom gravitationskraften med alla andra himlakroppar, även om solen är helt dominerande genom sin stora massa och relativt korta avstånd, även om till viss del även månen påverkar jorden, främst i form av tidvattenfenomen. Jorden roterar ett varv runt solen på 365,242 19 dagar.[12] För att kompensera för att det ej är ett jämnt antal dagar finns skottår. Jordens rotationsaxel är vinklad 23,4° mot en linje som är vinkelrät mot omloppsplanet, vilket skapar årstider på ytan. Jordens enda naturliga satellit, månen, orsakar havens tidvatten, stabiliserar axellutningen och saktar långsamt ner planetens rotation. Ett bombardemang av kometer under jordens tidiga historia gav upphov till mycket av vattnet i haven. Sedan dess har nedslag av större asteroider vid ett flertal tillfällen orsakat våldsamma katastrofer på jordens yta, mest känd är den som troligen orsakade utrotningen av den tidigare djurtypen dinosaurier (för cirka 65 miljoner år sedan). Planetens mineral och de många produkterna av biosfären bidrar med resurser som används för att försörja jordens befolkning. Invånarna är uppdelade i omkring 200 självständiga stater som samverkar med varandra genom diplomati, resor, handel och militära handlingar. Den första levande varelsen i omloppsbana runt jorden var hunden Lajka som med människans hjälp skickades upp i en satellit 1957. Människan själv lämnade jorden första gången 1961 då Jurij Gagarin nådde inre rymden."
    q = prompt

    answer_output = answerer({
        'question': q,
        'context': doc
    })
    answer = answer_output['answer']
    return answer

# model = BartForConditionalGeneration.from_pretrained(mask_model)
# tok = AutoTokenizer.from_pretrained(mask_model)
# model.eval()

# input_ids = tok.encode(
#     "Jag har ätit en utsökt <mask> på restaurang vid <mask> .", return_tensors="pt"
# )
# # Beam search
# output_ids = model.generate(
#     input_ids,
#     min_length=15,
#     max_length=25,
#     no_repeat_ngram_size=3,
#     num_beams=8,
#     early_stopping=True,
#     do_sample=True,
#     num_return_sequences=6
# )
# tok.decode(output_ids[0])

# print(output_ids[0])
