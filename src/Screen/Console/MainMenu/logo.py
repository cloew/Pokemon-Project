from Screen.Console.view import View

class Logo(View):
    """ Represents the Logo on the screen """
    
    def __init__(self):
        """ Builds the logo """
        self.logo = ['                                 .::.                          ''',
                         '                              .;:**\'            AMC           ',
                         '                              `                  0            ',
                         '  .:XHHHHk.              db.   .;;.     dH  MX   0            ',
                         'oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN     ',
                         'QMMMMMb  "MMX       MMMMMMP !MX\' :M~   MMM MMM  .oo. XMMM \'MMM',
                         '  `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP',
                         '   \'MMMb.dM! XM M\'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" MX MMXXMM ',
                         '    ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP ',
                         '     ?MMM>  YMMMMMM! MM   `?MMRb.    `"""   !L"MMMMM XM IMMM  ',
                         '      MMMX   "MMMM"  MM       ~%:           !Mh.""" dMI IMMP  ',
                         '      \'MMM.                                             IMX   ',
                         '       ~M!M                                             IMP   ']
        
    def draw(self, window):
        """ Draws the logo """
        lines = []
        for line in self.logo:
            lines.append(window.terminal.yellow(line))
        return lines