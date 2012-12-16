from Screen.Console.view import View

class Logo(View):
    """ Represents the Logo on the screen """
    
    def __init__(self):
        """ Builds the logo """
        self.logo = ['                                 .::.                         ',
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
        lineLength = len(self.logo[0])
        for line in self.logo:
            if not len(line) == lineLength:
                print len(line), lineLength
                raise Exception("{0} is not {1}\r\n{2}".format(len(line), lineLength, line))
        
            lines.append(window.terminal.yellow(line))
        return lines, (len(self.logo[0]), len(lines))