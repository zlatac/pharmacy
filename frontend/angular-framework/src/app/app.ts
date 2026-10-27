import { Component, signal, computed, inject } from '@angular/core';
import {FormsModule} from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import {MatInput} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatChipsModule} from '@angular/material/chips';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import {MatSelectModule} from '@angular/material/select';
import {MatSnackBar} from '@angular/material/snack-bar';
import prescriptionExamples from '../json/prescription-examples.json';

@Component({
  imports: [RouterOutlet, FormsModule, MatInput, MatFormFieldModule, MatChipsModule,MatProgressBarModule, MatSelectModule],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('angular-framework');
  loading = signal(false)
  loaderClasses = computed(() => !this.loading() ? 'hide' : '')
  quantityPrefix = signal(0)
  prefixTranslation = computed(
    () => this.showPrefix() && this.quantityPrefix() > 0 ? `${this.quantityPrefix()} ` : ''
  )
  showPrefix = signal(false)
  sigSearch = ''
  example = ''
  translation = signal({fullTranslation: ''})
  codeList: string[] = []
  chips = signal<undefined | string[]>(undefined)
  prescriptions = prescriptionExamples
  private _snackBar = inject(MatSnackBar)

  async ngOnInit() {
    try {
      this.loading.set(true)
      const res = await fetch('http://localhost:8000/keys', {mode: 'cors'})
      this.codeList = await res.json()
    } catch (error) {
        this._snackBar.open('Failed to setup page', undefined,  {
            duration: 5000,
            verticalPosition: 'top'
        })
    } finally {
        this.loading.set(false)
    }
  }

  generateChips() {
    this.showPrefix.set(false)
    if (this.sigSearch.trim() === '') {
      this.translation.set({fullTranslation: ''})
      this.chips.set([])
      this.quantityPrefix.set(0)
      return
    }
    const search = this.sigSearch.replaceAll('.', '')
    const output: string[] = []
    search.split(' ').forEach((item, index) => {
      const formatedItem = item.toLowerCase()
      if (this.codeList.includes(formatedItem)) {
        output.push(formatedItem)
      }
      if (index === 0) {
        if ( Number.isFinite(Number(formatedItem))) {
          this.quantityPrefix.set(Number(formatedItem))
        } else {
          this.quantityPrefix.set(0)
        }
      }
    })
    this.chips.set(output)
  }

  async translate() {
    try {
      this.loading.set(true)
      if (Array.isArray(this.chips()) && this.chips()?.length === 0) {
        throw new Error('No Pharmacy Sig codes found')
      }
      const res = await fetch(`http://localhost:8000/?codes=${this.chips()?.join(' ')}`, {mode: 'cors'})
      const formatted = await res.json()
      this.translation.set(formatted)
      this.showPrefix.set(true)
    } catch (error) {
        const msg = error instanceof Error ? error.message : 'Failed to translate'
        this._snackBar.open(msg, undefined,  {
          duration: 5000,
          verticalPosition: 'top'
        })
    } finally {
        this.loading.set(false)
    }
  }

  async exampleChanged() {
    if (this.example !== '') {
      this.sigSearch = this.example
      this.generateChips()
      await this.translate()
    }
  }
}
