import user_module as um 

import privileges_admin_module as pam 

administrador = um.Admin('Romano', 'Delgado', 24, 'Masculino')
#administrador.greet_user()
#administrador.describe_user()
administrador.privilegess.show_privileges()