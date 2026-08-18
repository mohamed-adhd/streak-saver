using CommunityToolkit.Mvvm.Input;
using CommunityToolkit.Mvvm.ComponentModel;

namespace ssaver.ViewModels;


public partial class configsViewModel : ViewModelBase
{
    [ObservableProperty] private MainWindowViewModel _main;
    public configsViewModel(MainWindowViewModel main)
    {
        _main = main;
        
    }
    [RelayCommand]
    public void onVerifyClicked()
    {
        return;
    }
}
