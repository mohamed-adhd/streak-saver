using CommunityToolkit.Mvvm.Input;
using CommunityToolkit.Mvvm.ComponentModel;

namespace ssaver.ViewModels;

public partial class welcomeViewModel : ViewModelBase
{
    [ObservableProperty] private ViewModelBase current_page;
    [ObservableProperty] private MainWindowViewModel _main;

    public welcomeViewModel(MainWindowViewModel main)
    {
        _main = main;
        
    }
    [RelayCommand]
    public void clik()
    {
        _main.Current_page = new configsViewModel();
    }
    
}
