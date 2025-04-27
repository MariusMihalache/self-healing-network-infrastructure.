# self-healing-network-infrastructure.
Automatizarea reparării infrastructurii de rețea folosind Ansible, Python și machine learning
# Self-Healing Network Infrastructure

## Descriere
Acest proiect utilizează Ansible, Python și Machine Learning pentru a crea o infrastructură de rețea autonomă, capabilă să detecteze și să repare problemele comune (precum DNS, gateway sau ping). Scopul este de a reduce downtime-ul rețelei și de a spori eficiența operațiunilor de rețea.

## Cum funcționează
- **Ansible** detectează problemele de rețea și rulează playbook-uri pentru a le remedia.
- **Python** monitorizează rețeaua și învață să prevadă problemele viitoare.
- **Bash** oferă scripturi rapide de verificare și reparare pentru probleme de bază.

## Pași de implementare:
1. **Detectarea** - Cum rulezi detectarea problemelor:
    - Detalii despre fișierul `playbook-detect.yaml`.
2. **Repararea** - Cum rulezi repararea:
    - Detalii despre fișierul `playbook-repair.yaml`.
3. **Mini AI** - Cum antrenezi și folosești modelul ML:
    - Detalii despre fișierul `ml_model.py`.

## Instalare
1. Clonează repository-ul: 
    ```bash
    git clone https://github.com/tuser/self-healing-network-infrastructure.git
    ```
2. Instalează dependențele:
    ```bash
    pip install -r requirements.txt
    ```

## Contribuții
Contribuțiile sunt binevenite! Fă un fork al repository-ului și trimite un pull request.
