from odoo import models, fields, api
import base64
import tempfile
import whisper
import os

class AudioNote(models.Model):
    _name = 'audio.note'
    _description = 'Audio Note'

    name = fields.Char(string="Title")
    audio_file = fields.Binary(string="Audio File")
    filename = fields.Char(string="Filename")
    transcription = fields.Text(string="Transcription")

    property_id = fields.Many2one('estate.property', string="Propiedad")  # Relación con propiedad alquiler
    @api.model
    def transcribe_with_whisper(self, audio_base64, filename):
        # Guardar el archivo temporalmente
        with tempfile.NamedTemporaryFile(delete=False, suffix=filename[-4:]) as temp_audio:
            temp_audio.write(base64.b64decode(audio_base64))
            temp_audio.flush()
            temp_path = temp_audio.name

        try:
            model = whisper.load_model("base")  # Puedes cambiar a tiny, small, medium, large según el rendimiento/calidad
            result = model.transcribe(temp_path, language="es")
            return result['text']
        except Exception as e:
            return f"Error en transcripción: {str(e)}"
        finally:
            os.remove(temp_path)

    def action_transcribe(self):
        for record in self:
            if record.audio_file and record.filename:
                transcription = self.transcribe_with_whisper(record.audio_file, record.filename)
                record.transcription = transcription
