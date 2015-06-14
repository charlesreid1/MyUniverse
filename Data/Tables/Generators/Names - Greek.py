from random import choice
from random import randint

class generator:
    def version(self):
        return 1.0

    def start(self):
        return choice([self.pre() + self.suf(), self.begin() + self.middle() + self.end()]).capitalize()

    def pre(self):
        elements = ["ab", "abad", "abel", "abyss", "ad", "adelph", "adiak", "adik", "adok", "adyn", "aer", "aeth", "agall", "agamemn", "agap", "agath", "ageneal", "agenealog", "agn", "agog", "agor", "agorax", "aichmal", "aid", "ain", "ainigm", "aion", "air", "aisch", "aischr", "aischrot", "aisth", "aisthan", "aisthet", "ait", "aitem", "ak", "akair", "akak", "akarp", "akatakr", "akatast", "akathars", "akathart", "aker", "akolouth", "akrogon", "akrop", "akyr", "alal", "alalaz", "alaz", "alazon", "aleiph", "aleth", "all", "alleg", "allel", "allog", "alloph", "allos", "allotr", "allotriep", "alog", "alyp", "am", "amempt", "amen", "ametan", "amiant", "amn", "amom", "amp", "ampel", "an", "anabain", "anadeikn", "anadeix", "anagen", "anagenn", "anagin", "anagn", "anakain", "anakr", "analamb", "analemp", "analemps", "analog", "analys", "anamart", "anamartet", "anamn", "anan", "anang", "anangel", "anankamom", "anap", "anaph", "anapl", "anaps", "anast", "anastaur", "anastr", "anat", "anathem", "anatith", "anatol", "anax", "anaz", "andr", "andriz", "anech", "anekt", "aneleem", "anenkl", "anepil", "aner", "anes", "anex", "anexer", "anexereun", "anexichn", "anexik", "anexikak", "ang", "angel", "aniem", "anipt", "anist", "anoch", "anos", "anot", "anoth", "ant", "antagon", "antall", "antallagm", "antan", "antanapl", "antap", "antapodid", "anthom", "anthomol", "anthomolog", "anthropar", "antilamb", "antilemp", "antilytr", "antimisth", "antityp", "anypotakt", "aorat", "apait", "apall", "apallotr", "apang", "apangel", "apant", "aparab", "aparch", "aparn", "apat", "apaug", "apeith", "apekd", "apeleuth", "apelp", "aperitm", "aph", "aphil", "aphilag", "apier", "apist", "apod", "apodech", "apodid", "apogign", "apokarad", "apokatall", "apokatast", "apokath", "apokol", "apoll", "apolytr", "apophtheng", "apops", "aposk", "apost", "aposyn", "apoth", "apothn", "aprosk", "aprosopol", "ar", "arch", "archang", "aren", "aresk", "aret", "arg", "aridion", "arist", "arithm", "ark", "arn", "arneom", "arrab", "arret", "art", "artigenn", "as", "aseb", "aselg", "ask", "asot", "aspasm", "aspaz", "asphal", "aspil", "ast", "astat", "asth", "asthen", "astr", "asyn", "atakt", "ath", "athanas", "athem", "athen", "athesm", "athet", "athl", "aug", "autark", "auth", "authad", "ax", "b", "bain", "bapt", "bar", "barb", "barbar", "basan", "basil", "basilik", "bask", "bast", "bath", "battal", "battar", "bdelygm", "bdelykt", "bdelyss", "beb", "bebel", "bel", "biast", "biaz", "bibl", "blasph", "blep", "boul", "brab", "brach", "brom", "bront", "bros", "brych", "brygm", "bybl", "ch", "chair", "char", "charagm", "charism", "charit", "charybd", "cher", "chil", "chliar", "chr", "chremat", "chrest", "chrisn", "christ", "chrom", "chron", "d", "daim", "daimon", "daktyl", "dech", "dees", "deikn", "deipn", "deisidaimon", "dek", "dekt", "deom", "desm", "despot", "dex", "diabol", "diagong", "diair", "diak", "dial", "diall", "dialog", "diamartyr", "diang", "diangel", "diaph", "diaphth", "diask", "diastr", "diat", "diath", "dichost", "did", "didakt", "dierch", "diermen", "diex", "dik", "diorth", "dips", "disk", "doch", "dodek", "dogm", "dok", "dokim", "dor", "doul", "dox", "drak", "drom", "dyn", "dynam", "dynat", "dysn", "ech", "echidn", "echth", "echthr", "eid", "eidol", "eik", "eim", "eir", "eiren", "eis", "eisak", "eiserch", "eisk", "eisod", "eisph", "eispor", "ekb", "ekbal", "ekch", "ekchyn", "ekd", "ekdik", "ekkath", "ekkent", "ekkl", "ekkopt", "ekkrem", "ekl", "eklamp", "ekleg", "eklekt", "ekmykt", "ekneph", "ekpipt", "ekpn", "ekporn", "ekriz", "ekten", "ektenest", "ekthamb", "ektrom", "el", "elach", "eleem", "elegm", "elench", "elenx", "eleuth", "ellog", "elp", "embat", "emm", "emperip", "emph", "emphys", "empn", "en", "endem", "endox", "eng", "enkak", "enkal", "enklem", "enkr", "enkrat", "enn", "enoch", "ent", "entell", "enthym", "ep", "epagon", "epair", "epaisch", "epak", "epakol", "epakolouth", "epanap", "epang", "epanorth", "epar", "eparat", "ephap", "epib", "epig", "epign", "epik", "epikatar", "epil", "epilys", "epis", "episk", "epistr", "epistre", "epit", "epithes", "epitith", "er", "erem", "ereun", "erg", "ergas", "ergat", "erith", "erot", "esch", "eschat", "esop", "esoptr", "est", "esth", "eth", "ethel", "ethn", "euarest", "euch", "euchom", "euk", "eulab", "eurisk", "euseb", "ex", "exagor", "exait", "exakolouth", "exanast", "exang", "exanist", "exap", "exapat", "exapost", "exaragoraz", "exart", "exeg", "exer", "exerch", "exest", "exist", "exod", "exolothr", "exomol", "exork", "exypn", "g", "gal", "galat", "gam", "geenn", "gegr", "gel", "gen", "geneal", "genn", "geuom", "gign", "gin", "ginosk", "gloss", "gnes", "gnom", "gnor", "gnos", "goes", "gon", "gong", "gongysm", "gongyst", "gonyp", "gorg", "gramm", "graph", "gymn", "gyn", "h", "had", "hag", "hagiasm", "hagiot", "hagn", "hagnism", "haim", "haimatek", "haimatekch", "hair", "hairetik", "hal", "hamart", "hap", "hapl", "harp", "harpagm", "hekon", "hel", "helik", "hem", "herk", "herod", "hetair", "heter", "hetoim", "hier", "hikan", "hiket", "hilar", "hilask", "hilasm", "hilast", "hip", "hist", "hodeg", "hol", "holokl", "holot", "hom", "homol", "hopl", "hor", "hork", "horm", "hos", "hot", "hout", "hyb", "hybrist", "hyd", "hyg", "hymn", "hyp", "hypak", "hypek", "hypn", "hypod", "hypokr", "hypomn", "hyst", "iak", "iam", "iamb", "iann", "iatr", "ichn", "ichth", "icles", "id", "idiot", "ierem", "ion", "ios", "ir", "isang", "isangel", "isch", "isot", "k", "kain", "kair", "kak", "kal", "kalym", "kalypt", "kamel", "kamph", "kard", "karp", "karter", "katab", "katad", "katagel", "katagon", "kataisch", "katall", "katang", "katangel", "katar", "katarasth", "katarg", "katart", "katathem", "katax", "kateg", "kath", "kathap", "kathar", "kathek", "kathist", "kaum", "keim", "kelt", "kenod", "kent", "keph", "kephal", "kerd", "kin", "klas", "klasm", "klauthm", "kleis", "klem", "klept", "kler", "kleron", "knoss", "koin", "kokk", "kol", "kolak", "kolaph", "koloss", "kolp", "kopt", "korb", "kosm", "kr", "krasp", "krat", "krem", "kreman", "krin", "krit", "ktis", "ktist", "kymb", "kyr", "l", "lach", "lakt", "lal", "lamb", "lamp", "lanch", "latr", "leg", "likm", "lim", "linab", "lith", "log", "loid", "loutr", "lychn", "lyk", "lyp", "lytr", "m", "main", "makar", "makel", "makr", "malak", "manth", "maran", "mart", "mas", "mast", "mat", "math", "mathet", "med", "meg", "megal", "mel", "memph", "memps", "men", "mer", "mes", "metall", "metan", "meth", "metoch", "metr", "mikr", "mimet", "mimn", "misth", "mn", "mog", "mol", "mom", "momph", "mon", "mor", "morph", "mosch", "mykt", "myr", "myst", "myth", "n", "nekr", "neom", "nep", "neph", "nest", "nik", "nipt", "nom", "nomik", "nomoth", "nos", "nothr", "nouth", "nymph", "nyn", "nyx", "ochl", "ochyr", "od", "odyn", "odyr", "odyrm", "odyss", "oid", "oik", "oikodesp", "oikonom", "oiktir", "olig", "oligop", "olol", "oloth", "olothr", "olymp", "omn", "on", "onk", "onom", "oph", "ophiel", "ophthal", "opis", "opisth", "opson", "opt", "optan", "or", "oreg", "orex", "org", "orgil", "orph", "orth", "osph", "ot", "otar", "ouran", "ous", "ox", "p", "pach", "pagis", "paid", "pal", "palingen", "pang", "papyr", "par", "parab", "parabl", "parag", "parait", "parak", "parakolouth", "paramen", "paren", "pares", "parous", "parox", "parrh", "parthen", "pat", "path", "patr", "patrik", "peg", "pegas", "peith", "pelasg", "pemp", "penth", "per", "perik", "peril", "perim", "perips", "perit", "ph", "phan", "phant", "phatn", "pher", "phil", "philadelph", "philag", "philip", "phob", "phon", "phor", "phort", "phos", "phosph", "phost", "phot", "phr", "phron", "phth", "phyl", "phylak", "phys", "pier", "pieth", "pimpl", "pin", "pipt", "pist", "pkr", "pl", "plan", "plass", "plast", "plen", "pleon", "pler", "pleth", "pn", "pneum", "poim", "polit", "polyl", "pom", "pon", "por", "porn", "pos", "pot", "pr", "prag", "pragm", "prakt", "pras", "praut", "prax", "presb", "proag", "prog", "progin", "progn", "progr", "prograph", "prok", "prokatang", "prom", "prosag", "prosagog", "prosanatith", "prosdeom", "prosk", "prosopol", "prost", "prot", "proth", "psalm", "psalt", "pseph", "pseust", "psych", "pt", "ptom", "ptos", "ptyx", "pygm", "pyk", "pykt", "pyl", "pyr", "pyrr", "pyth", "rh", "rhab", "rhabd", "rhad", "rhant", "rhem", "rhipt", "rhomb", "rhomp", "rhyom", "romph", "s", "sain", "sakk", "sal", "salp", "sam", "sark", "seb", "sem", "set", "sik", "sin", "sk", "skand", "sken", "skirt", "skler", "skol", "skolek", "skop", "skorp", "skot", "skyb", "smyrn", "som", "soph", "sophr", "sor", "sot", "spart", "speir", "sph", "sphrag", "splanchn", "st", "stas", "staur", "steg", "stek", "stel", "sten", "ster", "stigm", "stilb", "stoich", "stom", "str", "strat", "streph", "styl", "syk", "sykom", "sykoph", "syl", "syllamb", "syllyp", "symbas", "symph", "syn", "synag", "synaichmal", "synakolouth", "synantilamb", "synathl", "syngn", "synist", "synk", "synkl", "synt", "syntr", "syss", "syst", "syz", "t", "tagm", "tap", "tas", "tekn", "tel", "temn", "ter", "tessar", "tessarak", "tetart", "th", "thamb", "than", "thanat", "tharr", "thars", "thaum", "thel", "themel", "theodid", "theokr", "theom", "theor", "theos", "theot", "ther", "therap", "thesaur", "thessalon", "thlips", "thnesk", "thnet", "thor", "thren", "thresk", "thron", "thym", "thyr", "thys", "tim", "tith", "tithem", "tolm", "top", "tr", "trap", "trech", "trit", "trog", "tryg", "tynch", "typ", "typhl", "typik", "xen", "xyl", "yon", "z", "zel", "zelot", "zem", "zest", "zet", "zon", "zonn", "zoog", "zoop", "zyg", "zym"]
        return choice(elements)

    def suf(self):
        elements = ["a", "aea", "aean", "aeuo", "age", "agma", "ai", "aino", "aio", "aios", "aira", "airia", "airo", "akos", "alaia", "aleo", "alia", "alizo", "almos", "alotos", "alypto", "amai", "ambano", "aminos", "ano", "anomai", "anon", "anteo", "ao", "aom", "aomai", "aos", "ar", "archeo", "ardia", "arenos", "argeo", "arios", "arites", "arma", "aros", "arotes", "arx", "as", "ascho", "asia", "asis", "askalos", "asma", "asso", "astole", "ateia", "ateus", "atheke", "athes", "athos", "atoo", "atos", "atres", "auid", "auo", "auroo", "auson", "ax", "axus", "azo", "e", "echos", "ege", "eia", "eias", "eilema", "eimma", "einos", "eion", "eioo", "eios", "eira", "eirao", "eksos", "eleuo", "eleus", "elia", "elion", "ello", "ellon", "elomai", "elos", "ema", "emai", "emeo", "empsia", "enion", "enis", "enos", "ens", "enteo", "eo", "eomai", "eon", "eoreo", "eos", "ephele", "epho", "eras", "erdos", "eresis", "ergos", "erion", "eron", "eros", "eryno", "eryx", "es", "es", "esia", "esis", "esko", "etes", "etos", "euma", "eunao", "euo", "euomai", "euos", "eus", "eusma", "euxis", "exia", "ia", "ias", "iasis", "iasmos", "iastos", "iazo", "ikao", "ikles", "ileo", "ilioi", "imos", "inia", "ino", "inoi", "inos", "ion", "ios", "iosyne", "iotes", "ipto", "irmon", "irmos", "is", "isis", "iskopos", "ismos", "ites", "itos", "ix", "izo", "o", "oche", "oe", "oema", "oeo", "oer", "oetheia", "oetos", "og", "oge", "ogeo", "ogia", "oia", "oichon", "oida", "oietos", "okles", "olex", "ologeo", "ologia", "olos", "omai", "omeo", "omos", "omphe", "on", "onia", "onios", "onos", "oo", "oomai", "oon", "oos", "ophe", "opia", "opia", "opoe", "opon", "opos", "ops", "ora", "oras", "oreo", "oria", "orimos", "oros", "orphos", "os", "osia", "osis", "osko", "oste", "ostos", "osyne", "otes", "oteuo", "othen", "otizo", "otle", "otos", "otus", "oul", "oulia", "ouni", "ouo", "outheo", "outhion", "oxazo", "oxos", "uios", "ygma", "ykos", "ylon", "ylos", "ymeo", "ymi", "ymia", "ymma", "ymos", "yn", "yno", "ynthos", "ynx", "yo", "ypte", "ypto", "yreo", "yria", "yrion", "yrna", "yroma", "yromai", "yros", "ys", "ysia", "ysmos", "ysso", "ystes", "yteros", "ythos", "ytos", "yx", "yxis", "yzo"]
        return choice(elements)

    def begin(self):
        elements = ["ant", "ap", "aph", "ar", "ascl", "art", "ath", "atl", "c", "cr", "d", "dem", "dion", "epim", "er", "g", "h", "hel", "heph", "iap", "hyp", "m", "mn", "oc", "pers", "ph", "pos", "prom", "rh", "t", "th", "ur", "z"]
        return choice(elements)

    def middle(self):
        elements = ["a", "ae", "e", "ea", "ei", "emo", "eu", "i", "ia", "io", "iu", "o", "oe", "y"]
        return choice(elements)

    def end(self):
        elements = ["be", "ctor", "dite", "don", "lius", "llo", "mis", "na", "ne", "nus", "phon", "phone", "pius", "rion", "rmes", "rus", "s", "stia", "stus", "sus", "syne", "ter", "theus", "thys", "tus", "u"]
        return choice(elements)




#x = generator()
#print x.start()
