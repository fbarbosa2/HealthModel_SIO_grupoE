<template>
    <div class="background">
        <div class="form-container">
            <h1>Formulário sobre a sua saúde</h1>
            <h2>Descubra a probabilidade de ter algum tipo de doença através do nosso modelo!</h2>
            <form @submit.prevent="handleSubmit">
                <label for="fever">Febre</label>
                <select v-model="form.fever" id="fever">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="cough">Tosse</label>
                <select v-model="form.cough" id="cough">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="fatigue">Fadiga</label>
                <select v-model="form.fatigue" id="fatigue">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="breathing">Dificuldade Respiratória</label>
                <select v-model="form.breathing" id="breathing">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="age">Idade</label>
                <input type="number" v-model="form.age" id="age" min="0" required />

                <label for="gender">Género</label>
                <select v-model="form.gender" id="gender">
                    <option value="Male">Masculino</option>
                    <option value="Female">Feminino</option>
                </select>

                <label for="bp">Pressão Arterial</label>
                <select v-model="form.bp" id="bp">
                    <option value="Normal">Normal</option>
                    <option value="High">Alta</option>
                    <option value="Low">Baixa</option>
                </select>

                <label for="cholesterol">Colesterol</label>
                <select v-model="form.cholesterol" id="cholesterol">
                    <option value="Low">Baixo</option>
                    <option value="Normal">Normal</option>
                    <option value="High">Alto</option>
                </select>

                <label for="sore-throat">Garganta Seca</label>
                <select v-model="form.sore_throat" id="sore-throat">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="chest-pain">Dor no peito</label>
                <select v-model="form.chest_pain" id="chest-pain">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="skin-rash">Erupção cutânea</label>
                <select v-model="form.skin_rash" id="skin-rash">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="nausea">Náuseas</label>
                <select v-model="form.nausea" id="nausea">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="muscle-pain">Dores Musculares</label>
                <select v-model="form.muscle_pain" id="muscle-pain">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="loss-of-appetite">Perda de Apetite</label>
                <select v-model="form.loss_of_appetite" id="loss-of-appetite">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>

                <label for="dizziness">Tonturas</label>
                <select v-model="form.dizziness" id="dizziness">
                    <option value="Yes">Sim</option>
                    <option value="No">Não</option>
                </select>
                <button type="submit">Submeter</button>

                <div v-if="result" class="result-box">
                    <div class="result-text">
                        <strong>Diagnóstico previsto:</strong><br/>
                        <pre>{{ result }}</pre>
                    </div>
                </div>

            </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                fever: 'No',
                cough: 'No',
                fatigue: 'No',
                breathing: 'No',
                age: 0,
                gender: 'Male',
                bp: 'Normal',
                cholesterol: 'Normal',
                sore_throat: 'No',
                chest_pain: 'No',
                skin_rash: 'No',
                nausea: 'No',
                muscle_pain: 'No',
                loss_of_appetite: 'No',
                dizziness: 'No'
            },
            result: ''
        };
    },
    methods: {
        async handleSubmit() {
            try {
                const response = await fetch('http://localhost:5000/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.form)
                });
                const data = await response.json();
                this.result = data.result;
            } catch (error) {
                console.error('Erro ao submeter:', error);
                this.result = 'Erro ao obter diagnóstico.';
            }
        }
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

.background {
    min-height: 100vh;
    background: linear-gradient(135deg, #1e3c72 0%, #3360ad 50%, #6ca7ce 100%);
    display: flex;
    align-items: center;
    justify-content: center;
}

.form-container {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 2rem;
    width: 100%;
    max-width: 700px;
    color: #fff;
    font-family: 'Inter', sans-serif;
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    margin-top: 30px;
    margin-bottom: 30px;
}

h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    color: #ffffff;
}

h2 {
    font-size: 1rem;
    margin-bottom: 1.5rem;
    color: #e9e6e6;
}

form {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

label {
    font-weight: 600;
    margin-top: 0.5rem;
}

input,
select {
    padding: 10px;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    background-color: rgba(255, 255, 255, 0.2);
    color: #fff;
    transition: background-color 0.3s;
}

input:focus,
select:focus {
    background-color: rgba(255, 255, 255, 0.3);
    outline: none;
}

button {
    margin-top: 1rem;
    padding: 12px;
    background: linear-gradient(135deg, #2196f3, #1e88e5);
    border: none;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    cursor: pointer;
    transition: background 0.3s ease;
}

button:hover {
    background: linear-gradient(135deg, #1976d2, #1565c0);
}

.result {
    margin-top: 1rem;
    font-weight: bold;
    font-size: 1.1rem;
    color: #ffffff;
}

select option {
    color: black;
}

.result-box {
    margin-top: 2rem;
    padding: 1.5rem;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(6px);
    color: #fff;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    animation: fadeIn 0.6s ease-in-out;
}

.result-text {
    font-size: 1.2rem;
    line-height: 1.5;
    font-family: 'Inter', sans-serif;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>