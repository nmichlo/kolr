

from collections import namedtuple

# Escape Character: octal=\033 ∙ hex=\x1B ∙ decimal=27 ∙ keyboard=^[
ESC = '\033'


# C1 (8-Bit) Control Characters
# https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-C1-_8-Bit_-Control-Characters
_CtrlChar = namedtuple('ControlCharacter', ('bits7', 'bits8', 'name', 'lname', 'note'))
IND   = _CtrlChar(bits7=ESC + 'D',  bits8='\x84', name='IND',   lname='Index',                                          note="")
NEL   = _CtrlChar(bits7=ESC + 'E',  bits8='\x85', name='NEL',   lname='Next Line',                                      note="")
HTS   = _CtrlChar(bits7=ESC + 'H',  bits8='\x88', name='HTS',   lname='Tab Set',                                        note="")
RI    = _CtrlChar(bits7=ESC + 'M',  bits8='\x8d', name='RI',    lname='Reverse Index',                                  note="")
SS2   = _CtrlChar(bits7=ESC + 'N',  bits8='\x8e', name='SS2',   lname='Single Shift Select of G2 Character Set, VT220', note="This affects next character only.")
SS3   = _CtrlChar(bits7=ESC + 'O',  bits8='\x8f', name='SS3',   lname='Single Shift Select of G3 Character Set, VT220', note="This affects next character only.")
DCS   = _CtrlChar(bits7=ESC + 'P',  bits8='\x90', name='DCS',   lname='Device Control String',                          note="")
SPA   = _CtrlChar(bits7=ESC + 'V',  bits8='\x96', name='SPA',   lname='Start of Guarded Area',                          note="")
EPA   = _CtrlChar(bits7=ESC + 'W',  bits8='\x97', name='EPA',   lname='End of Guarded Area',                            note="")
SOS   = _CtrlChar(bits7=ESC + 'X',  bits8='\x98', name='SOS',   lname='Start of String',                                note="")
DECID = _CtrlChar(bits7=ESC + 'Z',  bits8='\x9a', name='DECID', lname='Return Terminal ID',                             note="Obsolete form of CSI c (DA).")
CSI   = _CtrlChar(bits7=ESC + '[',  bits8='\x9b', name='CSI',   lname='Control Sequence Introducer',                    note="")
ST    = _CtrlChar(bits7=ESC + '\\', bits8='\x9c', name='ST',    lname='String Terminator',                              note="")
OSC   = _CtrlChar(bits7=ESC + ']',  bits8='\x9d', name='OSC',   lname='Operating System Command',                       note="")
PM    = _CtrlChar(bits7=ESC + '^',  bits8='\x9e', name='PM',    lname='Privacy Message',                                note="")
APC   = _CtrlChar(bits7=ESC + '_',  bits8='\x9f', name='APC',   lname='Application Program Command',                    note="")

# # Single Character Functions
# # https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Single-character-functions
_SingleCharFunc = namedtuple('ControlCharacter', ('name', 'code', 'desc'))
BEL = _SingleCharFunc(name='BEL', code='Ctrl-G', desc="Bell (Ctrl-G).")
BS  = _SingleCharFunc(name='BS',  code='Ctrl-H', desc="Backspace (Ctrl-H).")
CR  = _SingleCharFunc(name='CR',  code='Ctrl-M', desc="Carriage Return (Ctrl-M).")
ENQ = _SingleCharFunc(name='ENQ', code='Ctrl-E', desc="Return Terminal Status (Ctrl-E).  Default response is an empty string, but may be overridden by a resource answerbackString.")
FF  = _SingleCharFunc(name='FF',  code='Ctrl-L', desc="Form Feed or New Page (NP).  (FF  is Ctrl-L).  FF  is treated the same as LF .")
LF  = _SingleCharFunc(name='LF',  code='Ctrl-J', desc="Line Feed or New Line (NL).  (LF  is Ctrl-J).")
SI  = _SingleCharFunc(name='SI',  code='Ctrl-O', desc="Switch to Standard Character Set (Ctrl-O is Shift In or LS0). This invokes the G0 character set (the default) as GL. VT200 and up implement LS0.")
SO  = _SingleCharFunc(name='SO',  code='Ctrl-N', desc="Switch to Alternate Character Set (Ctrl-N is Shift Out or LS1).  This invokes the G1 character set as GL. VT200 and up implement LS1.")
SP  = _SingleCharFunc(name='SP',  code='Space',  desc="Space.")
TAB = _SingleCharFunc(name='TAB', code='Ctrl-I', desc="Horizontal Tab (HT) (Ctrl-I).")
VT  = _SingleCharFunc(name='VT',  code='Ctrl-K', desc="Vertical Tab (Ctrl-K).  This is treated the same as LF.")
