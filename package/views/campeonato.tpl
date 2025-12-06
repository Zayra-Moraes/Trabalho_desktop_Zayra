<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" href="/static/img/black_2.png">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link href="/static/campeonato.css" rel="stylesheet">
    <title>{{campeonato.nome}}</title>
</head>
<body>


  <div class="d-flex flex-column min-vh-100">
    <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
        <a class="navbar-brand" href="#">
          <img src="/static/img/black_2.png" width="80" height="60">
        </a>
      <div class="container-fluid">
        <a class="navbar-brand" href="#">CampManager</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Campeonatos</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Equipes</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Cadastrados
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Atletas</a></li>
                <li><a class="dropdown-item" href="#">Técnicos</a></li>
    <!--            <li><hr class="dropdown-divider"></li>-->
    <!--            <li><a class="dropdown-item" href="#">Something else here</a></li>-->
              </ul>
    <!--        </li>-->
    <!--        <li class="nav-item">-->
    <!--          <a class="nav-link disabled" aria-disabled="true">Disabled</a>-->
    <!--        </li>-->
          </ul>
          </form>
        </div>
      </div>
    </nav>
    <main class="flex-grow-1">
        <div class="container classificacao">
            <br><h3 class="text-center">Tabela de Classificação</h3>

            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Pos.</th>
                        <th>Equipe</th>
                        <th>Pontos</th>
                        <th>Saldo</th>
                    </tr>
                </thead>

                <tbody>
                    % for linha in classificacao:
                    <tr>
                        <td>{{linha['posicao']}}</td>
                        <td>{{linha['nome']}}</td>
                        <td>{{linha['pontos']}}</td>
                        <td>{{linha['saldo']}}</td>
                    </tr>
                    % end
                </tbody>
            </table>
        </div>

    </main>

    <footer class="bg-dark text-white pt-4 pb-3 small">
        <div class="container">
            <div class="row">

                <div class="col-md-4">
                    <h5>CampManager</h5>
                    <p>Gerencie campeonatos, equipes e atletas rapidamente usando o CampManager, sem mais estresse para saber quem está ganhando!</p>
                </div>

                <div class="col-md-4">
                    <h5>Links úteis</h5>
                    <ul class="list-unstyled">
                        <li><a href="#" class="text-white">Vídeo_Nível4</a></li>
                        <li><a href="#" class="text-white">GitHub</a></li>
                    </ul>
                </div>

                <div class="col-md-4">
                    <h5>Contato</h5>
                    <p>Email: zayramoraes1212@gmail.com</p>
                </div>

            </div>

            <div class="text-center mt-3">
                © 2025 CampManager — Todos os direitos reservados.
            </div>
        </div>
    </footer>

  </div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>