# AI Engineer Journey — Tahir

**Start:** 7 Oct 2026
**Target:** 6-12 mahine me AI Engineer (GenAI / LLM App Developer) role
**Background:** Flutter / Dart developer

**Rules:**
1. Ek time pe ek hi step. Aage ka dump nahi.
2. Padhna nahi — banana. Har hafte kuch chalu hua ho.
3. 2 din se zyada atke to turant pooch lena.

---

## Progress

### Step 1 — Python (3 hafte)

- [x] Python 3.13.1 install
- [x] VS Code + Python extension
- [x] **Lesson 01** — variables, types, f-string, indentation, input()
  - [x] intro.py
  - [x] age_check.py
  - [x] calc.py
- [x] **Lesson 02** - list aur dict
  - [x] list_basics.py - index, append, remove, len
  - [x] loops.py - for-in, range, enumerate, loop+if
  - [x] dict_basics.py - key access, .get(), KeyError
  - [x] nested_data.py - .items(), nested dict, list of dicts, filter
- [x] **Lesson 03** - function aur file read/write
  - [x] functions.py - def, return, default param, list return karna
  - [x] files.py - with open, w/a/r mode, round trip (save + load)
- [x] **Lesson 04** - venv, pip, comprehension
  - [x] venv banaya + activate (.venv)
  - [x] pip install, pip freeze, requirements.txt
  - [x] encoding - UTF-8 vs UTF-16, BOM, cp1252
  - [x] comprehension.py - 7 point, loop vs comprehension side by side

**Lesson 04 ke seekhe sabak:** venv = **khaali** dabba (clone nahi, isolation), `requirements.txt` = Python ka pubspec.yaml, PowerShell ka `>` UTF-16 likhta hai (`Out-File -Encoding utf8` use karo), Windows pe `encoding="utf-8"` likhna zaroori hai, `utf-8-sig` BOM hata deta hai, aur comprehension = `[kya_chahiye for x in list if shart]`.

**Badi baat:** "sahi dikh raha hai" aur "sahi hai" do alag cheez hai - VS Code aur pip ne UTF-16 file chhupa li, apne `load_lines()` ne sach bataya.

**Lesson 03 ke seekhe sabak:** `def` (type nahi likhna), `return` ki **jagah** (loop ke bahar!), `return` na ho to `None`, default parameter, `with open()`, `"w"` = pehle mitao phir likho, `"a"` = jodo, `.strip()`, aur **`()` bhool gaye to function khud print hota hai, jawab nahi**.

**Lesson 02 ke seekhe sabak:** `enumerate()` aur `.items()` (do variable wala loop), `.get()` vs `[]` (KeyError se bachna), nested dict ka chained access, **list of dicts = AI API ka asli shape**, loop+if = filter, snake_case naming, aur "badalta hai to `None` deta hai" rule.

**Lesson 01 ke seekhe sabak:** f-string me `f` kyun lagta hai, `int(input())` nesting, function value *lautata* hai variable *badalta* nahi, `/` vs `//`, aur hardcoding ka bug (string me value type kar dena).

### Hafta 3 - Project (GitHub tool) - KHATAM

- [x] step1_pehla_call.py - requests.get, status_code, .json(), guard
- [x] step2_repos.py - list of dicts asli API se, filter, max nikalna
- [x] step3_save.py - text vs JSON save, json.dump/load, round trip
- [x] github_tool.py - poora tool: functions, input, sorting, 2 file save, error handling

**Project ke seekhe sabak:** `200 OK` ka matlab "sahi data mila" nahi hai (torvald vs torvalds - asli alag insaan), JSON null -> Python `None`, `x or "default"` idiom, `sorted(key=lambda ...)`, slicing `[:5]`, `json.dump(kya, kahan)`, **text file insaan ke liye / JSON program ke liye**, `try/except` apne bug ke liye nahi hota, aur `if __name__ == "__main__":`.

**Teen baar ek hi galti aayi:** galat block me line - `return` loop ke andar, `print` loop ke andar, `for` `with` ke bahar. Python me indentation hi structure hai.

### Step 2 - Claude API (shuru)

- [x] API key li + `.env` me rakhi, `.gitignore` me `.env`
- [x] check_key.py - masked key print
- [x] hello_claude.py - pehla call, usage, system prompt, stop_reason
- [x] chat.py - multi-turn conversation, history list, token growth
- [x] tool_use.py - TOOL USE (get_current_time + add_number, do tool ek saath)
- [x] **github_agent.py** - PEHLA ASLI AGENT (Week-03 ke functions + tool use)
- [x] **git + GitHub** - repo banaya, 2 commit, push ho gaya
  - github.com/sarmesh17/Ai-Journey (private)
- [x] **streaming.py + chat.py streaming** - jawab tukdon me, live
- [ ] agla: chat history save/load, phir prompt caching

**Streaming ke seekhe sabak:** `with client.messages.stream(...) as stream` (wahi `with` jo file me tha), `stream.text_stream` har tukda deta hai, `end=""` (warna har tukda nayi line) aur `flush=True` (warna output jama hota hai). `stream.get_final_message()` **loop ke baad** - tukdon ko jod kar wahi `response` object deta hai jo `create()` deta tha, isliye history wali line nahi badalti. Streaming jaldi/sasti nahi hai - sirf pehla shabd turant dikhta hai.

**Teesra encoding niyam:** `sys.stdout.reconfigure(encoding="utf-8")` - AI ke jawab me arrow/emoji aate hai, Windows ka cp1252 unko chhaap nahi paata.

**Git ke seekhe sabak:** `.gitignore` **pehle**, `git init` baad me (commit history se cheez hatana mushkil hai). `git status` folder band karke dikhata hai - `git status --porcelain -uall` se har file dikhti hai. `!.env.example` = apwaad (ye wali le lo). `git add -A` delete ko bhi pakadta hai. `git log --all --full-history -- "*.env"` se check karo ki secret kabhi gaya to nahi.

**Natija:** repo 188 KB (91 MB venv bahar), `.env` kabhi commit nahi hui.

**Agent banate waqt jo 7 galtiyan khud pakdi/theek ki:** `message=` (naam galat), `"roles"` (extra s), `user.get[...]` (`()` ki jagah `[]`), purana model, `n` hardcode (10), `tool_input["n"]` jabki `n` optional hai (`.get` chahiye), aur default do jagah likha (**DRY** - ek cheez ek hi jagah).

**Schema ka niyam:** `required` me hai -> `[]` safe. `required` me nahi -> `.get(key, default)` zaroori.

**Tool use ka nichod:** Claude = dimaag (sirf text padhta/likhta hai, code NAHI chalata). Python = haath (sab chalata hai). `tools` list sirf **description** hai, code nahi - Claude usi se chunta hai. Claude ek **string** bhejta hai (`block.name`), tumhara `if` use function se jodta hai. Ek sawaal = **do API call**. `tool_result` me **string** jaani chahiye (`str()`), aur `tool_use_id` match hona chahiye.

**User <-> Python <-> Claude** - beech wala hamesha tum ho. Claude kabhi khud se baat shuru nahi karta.

**Step 2 ke seekhe sabak:** API key kabhi code me nahi (`.env` + `python-dotenv` + `.gitignore`), least privilege (normal key, admin nahi), `messages` = wahi list of dicts jo Lesson 02 me banayi thi, `response.content` ek **list of blocks** hai (`content[0].text` galat aadat), `max_tokens` = ceiling (paisa sirf jitna bana utna), thinking tokens bhi `max_tokens` me ginte hai, `stop_reason` check karna zaroori, aur sabse bada: **Claude ke paas apni koi yaad nahi - history list TUMHARE paas hai, isliye lambi baat-cheet mehengi hoti hai.**

**Kharcha:** ek aam call ~$0.003 (Opus 5.5). ~315 call per dollar.

### Hafta ka naksha (sirf direction — abhi padhna nahi)
- Hafta 1 — core syntax: variables, list/dict, loop, function, file read/write
- Hafta 2 — Python ke tareeke: comprehension, f-string, virtual env, pip
- Hafta 3 — chhota project: API se data lao, process karo, file me save karo

### Step 2 — (Python ke baad khulega)

---

## Notes / doubts

- (jo samajh na aaye yahan likh lena, mentor se poochne ke liye)
